# Log-Analysis-Udacity-Project
This is an internal report tool for a news paper database. This program will tell user popular articles, popular anthers and which day does HTTP request fail in a high frequency.
(Project from [Full Stack Web Development Nanodegree](https://in.udacity.com/course/full-stack-web-developer-nanodegree--nd004/))

## Instructions
* <h4>Install <a href="https://www.vagrantup.com/">Vagrant</a> and <a href="https://www.virtualbox.org/wiki/Downloads">VirtualBox.</a></h4>
* <h4>Clone the repository to your local machine:</h4>
  <pre>git clone https://github.com/yanlinl/log-analysis-report</pre>
* <h4>Start the virtual machine</h4>
  Vagrant takes a configuration file called Vagrantfile that tells it how to start your Linux VM. Download the <a href="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f73b_vagrantfile/vagrantfile">Vagrantfile</a> here. Put this file into a new directory (folder) on your computer. Using your terminal, change directory (with the 'cd' command) to that directory, then run 'vagrant up'. 
  When vagrant up is finished running, you will get your shell prompt back. At this point, you can run `vagrant ssh` to log in to your     newly installed Linux VM.
* <h4>Download the <a href="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip">data</a></h4>
  You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant           directory, which is shared with your virtual machine.
* <h4>Setup Database</h4>
  To load the database use the following command:
  <pre>psql -d news -f newsdata.sql;</pre>
* <h4>Run Module</h4>
  <pre>python reportdb.py</pre>
  
