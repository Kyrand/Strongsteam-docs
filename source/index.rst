.. Strongsteam QuickStart documentation master file, created by
   sphinx-quickstart on Wed Apr  4 13:57:14 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Strongsteam QuickStart Guide
============================
Welcome to the `Strongsteam <http://strongsteam.com>`_ documentation !

`Strongsteam <http://strongsteam.com>`_ is a is an AppStore of artificial intelligence and
data mining APIs to let you pull interesting information
out of images, video and audio.

`Strongsteam <http://strongsteam.com>`_ is a cross-platform toolbox for developpers 
who want to "give a pair of eyes" to computers, or mobile devices, to recognize 
images, words, semantic context, etc.

All results sent from Strongsteam are `JSON <http://json.org/>`_-based. 
They thus can be interfaced with any programming language with `JSON <http://json.org/>`_ support:

* C
* C++
* C#
* D
* Java
* Javascript
* Matlab
* Objective-C
* Perl
* PHP
* Python
* R
* Ruby
* and many more...

Prerequisites and installation
------------------------------
Requirements
^^^^^^^^^^^^
* `Python <http://www.python.org/>`_ 2.6, 2.7 or 3.2
* `requests <http://docs.python-requests.org/en/latest/index.html>`_

Install Strongsteam
^^^^^^^^^^^^^^^^^^^
`Strongsteam <http://strongsteam.com>`_ is a cloud-based API, which means you do not need to install a whole bunch of packages or software.
Everything you need is hosted on our server: you just have to send us the data and we'll take care of the rest.

All you have to do is install the ``strongsteam`` python library.

We strongly suggest to install ``strongsteam`` in a virtual environnement, using `virtualenv <http://pypi.python.org/pypi/virtualenv>`_.

	$ virtualenv path/to/yourproject/
	$ source yourproject/bin/activate
	
.. Note :: 
	``virtualenv`` is a tool allowing you to create isolated python environnements. Read the `documentation <http://pypi.python.org/pypi/virtualenv>`_ to learn more about it.

You can install the ``strongsteam`` library in your virtual environnement with `pip <http://pypi.python.org/pypi/pip>`_, with the command ::

	pip install http://dl.dropbox.com/u/6113789/Strongsteam-client/strongsteam-0.0.1.tar.gz
	
.. Note ::
	For now, the module is privately hosted, but will be soon stored on PyPI. 	

.. Important ::
	Do not install the modules using ``sudo``: this will install them in your system python path and not in the virtual environnement.

First test
----------
To validate that the installation went well and that our server is running, you can run the `demo_hello_world.py <_static/py/demo_hello_world.py>`_ test script.

You should see something like this in your shell : ::

	$ python demo_hello_world.py
	Processing job on uri /user/kyran/processes/hello_world... 
	{
		u'status': u'succeeded', 
		u'time_stamps': 
		{
			u'ts_job_ps_end': 1333542151.78501, 
			u'ts_job_ws_receive': 1333542025.628467, 
			u'ts_job_js_receive': 1333542151.619243, 
			u'ts_job_ps_start': 1333542151.783706, 
			u'ts_job_post': u'1333542150.91'
		}, 
		u'input_uri': None, 
		u'process_name': u'hello_world', 
		u'results': 
		{
			u'hello_world_string': u'/user/kyran/vnd_ss_results/4f7c3d0711b3f4031f000000'
		}, 
		u'uri': u'/user/kyran/vnd_ss_results/4f7c3d0711b3f4031f000000', 
		u'job_uri': u'/user/kyran/jobs/4f7c3c89fa1d115c3500004b', 
		u'msg': u'Your job succeeded. Find the result-uris in results'
	}
	Job succeeded in 1.5700 seconds for /user/kyran/processes/hello_world
	Hello world ian!

.. Note ::
	Running this script can take more time (~30s) in the case where our server is asleep. Once awaken, everything will be blazing fast!
		
	
Send a job to Strongsteam
-------------------------
You can send us a job with just a few lines of code!

To understand how to do that, we'll go trough the `demo_hello_world.py <_static/py/demo_hello_world.py>`_ test script: ::

	from strongsteam.clients import ss_client as ssc
	from strongsteam.clients.ss_client import log

	# set log to INFO if you want lots of progress information or
	# use WARNING just to see the main client messages
	log.setLevel(ssc.logging.WARNING)

	if __name__ == "__main__":
		cli = ssc.StrongSteam()

		hello = cli.add_job(None, 'hello_world', data={'name':'oh, mighty Strongsteam user'})
		print hello.get_data()


Import, logging and API URL
---------------------------
You first need to import the ``ss_client`` class from the ``strongsteam.clients`` submodule, and setup a console logger. ::

	from strongsteam.clients import ss_client as ssc
	from strongsteam.clients.ss_client import log

	# set log to INFO if you want lots of progress information or
	# use WARNING just to see the main client messages
	log.setLevel(ssc.logging.WARNING)

You then need to setup a ``StrongSteam`` client: ::	

	cli = ssc.StrongSteam() # Set up a Strongsteam client 
	
	
Send a job
----------
	
Whenever you want to send us a job, just use the ``ss_client.StrongSteam.add_job()`` method: ::

	hello = cli.add_job(None, 'hello_world', data={'name':'oh, mighty Strongsteam user'}) # Add job of type "Hello world" 
	
.. Note::
	Do not invoke the ``cli.add_job(*args)`` without storing the result into a variable. You use ``hello`` 
	which is returned by ``add_job`` to query the status of the job and to extract results when the computation is finished.
	
	
The jobs we support
-------------------
Strongsteam being in alpha release, more jobs will be gradually added, as we mature.

OCR (Optical Character Recognition)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If you want to extract text information from images, you can send us to Strongsteam using the following API call: ::

	BlahBlah


You're stuck? Get help.
-----------------------
If you have any questions regarding `Strongsteam <http://strongsteam.com>`_, do not hesitate to send us an email at `help@strongsteam.com <mailto:help@strongsteam.com>`_.


