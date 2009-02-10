"""If it goes in zc.buildout this work will be reduced to 3 lines:

# add an attribute in zc.buildout.easy_install.Installer:
__picked_versions = {} 

# in the last loop in zc.buildout.easy_install.Installer._get_dist method
self.__picked_versions[dist.project_name] = dist.version 

#in the end of zc.buildout/buildout.py file
print zc.buildout.easy_install.Installer.__picked_versions 

"""

import os
import sys
import logging
import zc.buildout.easy_install
import pkg_resources

def enable_dumping_picked_versions(old_get_dist):
    def get_dist(self, requirement, ws, always_unzip):
        dists = old_get_dist(self, requirement, ws, always_unzip)
        for dist in dists:
            if not (dist.precedence == pkg_resources.DEVELOP_DIST or \
                    (len(requirement.specs) == 1 and requirement.specs[0][0] == '==')):
                self.__picked_versions[dist.project_name] = dist.version
        return dists        
    return get_dist


def dump_picked_versions(old_logging_shutdown, file_name=None):
    def logging_shutdown():
        picked_versions = '[buildout]\n\nversions = versions\n\n[versions]\n'
        for d, v in zc.buildout.easy_install.Installer.__picked_versions.items():
            picked_versions += "%s = %s\n" % (d, v)
        if file_name is not None:
            if os.path.exists(file_name):
                print "*************************************"
                print "File %s already exists." % file_name                 
                print "Please remove it to get a fresh copy"                
                print "*************************************"
            else:
                print "Writing picked versions to %s" % file_name
                open(file_name, 'w').write(picked_versions)
        else:
            print "*************** PICKED VERSIONS ****************"
            print picked_versions
            print "*************** /PICKED VERSIONS ***************"
        old_logging_shutdown()    
    return logging_shutdown


def install(buildout):
    file_name = 'dump-picked-versions-file' in buildout['buildout'] and \
                buildout['buildout']['dump-picked-versions-file'].strip() or \
                None
    zc.buildout.easy_install.Installer.__picked_versions = {}
    zc.buildout.easy_install.Installer._get_dist = enable_dumping_picked_versions(zc.buildout.easy_install.Installer._get_dist)
    logging.shutdown = dump_picked_versions(logging.shutdown, file_name)
    
