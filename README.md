# LearningDjango-1-4
- Linux/Mac

		cd LearningDjango-1-4/
		virtualenv -p python2.7 env
		. env/bin/activate
		pip install django==1.4.22
		# 如果访问慢，可以换一个国内的源，清华，豆瓣，阿里
		# pip install django==1.4.22 -i https://pypi.tuna.tsinghua.edu.cn/simple
		cd mysite/
		python manage.py runserver

- Windows

		cd LearningDjango-1-4/
		virtualenv -p C:\Python27\python.exe env
		call env\Scripts\activate
		pip install django==1.4.22
		# 如果访问慢，可以换一个国内的源，清华，豆瓣，阿里
		# pip install django==1.4.22 -i https://pypi.tuna.tsinghua.edu.cn/simple
		cd mysite/
		python manage.py runserver
