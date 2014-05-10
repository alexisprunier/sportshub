# -*- coding: utf-8 -*-


from fabric.api import *
import datetime

env.hosts = [ '37.187.7.168' ]
env.user = "antale"
path_prod = "/var/www/html/sportshub/"
directory_scr = "SportsHubScript"
directory_tmpl = "templates"
directory_views = "SportsHubApp"

def deploy(local_project_path, script):
    now = datetime.date.today()
    
    with cd(path_prod):
        
        ############
        # SCRIPTS  #
        ############
        
        if script == "yes":
            # Creation tar des script
            local("cd "+local_project_path)
            local("tar -cf scripts.tar "+directory_scr)
    
            #run("tar -cvf scripts_%s_%s_%s.tar %s" % (now.day,now.month,now.year,directory))
            run("rm -rf %s" % (directory_scr))
            
            # Detarer nouveau scripts
            put("scripts.tar", path_prod)
            run("tar -xvf %sscripts.tar" % (path_prod))
            run("rm %sscripts.tar" % (path_prod))
            
            # Nettoyage
            local("rm %sscripts.tar" % (local_project_path))
        
        #############
        # TEMPLATE  #
        #############
        
        # Creation tar des script
        local("cd "+local_project_path)
        local("tar -cf scripts.tar "+directory_tmpl)
        
        # Detarer nouveau scripts
        put("scripts.tar", path_prod)
        run("tar -xvf %sscripts.tar" % (path_prod))
        run("rm %sscripts.tar" % (path_prod))
        
        # Nettoyage
        local("rm %sscripts.tar" % (local_project_path))
        
        #############
        # VIEWS     #
        #############
        
        # Creation tar des script
        local("cd "+local_project_path)
        local("tar -cf scripts.tar "+directory_views)
        
        # Detarer nouveau scripts
        put("scripts.tar", path_prod)
        run("tar -xvf %sscripts.tar" % (path_prod))
        run("rm %sscripts.tar" % (path_prod))
        
        # Nettoyage
        local("rm %sscripts.tar" % (local_project_path))
        
        #######################
        # HTTPD RE-RUN        #
        #######################
        
        run("sudo service httpd restart")
    
        #######################
        # COLLECT STATICS     #
        #######################
        
        try:
            run("/home/antale/py-sportshub/bin/python2.6 %s/manage.py collectstatic" % (path_prod))
        except Exception as e:
            print str(e)
        
    
    
    
