# redis-python-client
redis-python-clientは、pythonで動作する(マイクロサービス)ランタイムにおいて、redis を使用する際に用いる、メタライブラリです。  
本ライブラリのインストールは、各システム環境やエッジコンピューティングデバイス内におけるランタイムの特性に応じて、必要に応じて行ってください。    

## 動作環境  

* OS: Linux  
* CPU: ARM/AMD/Intel  
* Python Runtime  

## 導入方法  
本リポジトリを pip でインストールしてください。  
```
pip install "git+https://github.com/latonaio/redis-python-client.git@main#egg=redis_client"
```

本リポジトリに格納されている setup.pyで、ライブラリの構築を行ってください。  

```python
setup(
	name='redis-python-client',
	version='0.1.0',
	description='redis client',
	long_description='redis client',
	packages=['redis_client'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		'redis==3.0.0', # この箇所に適切なバージョンに変更してください
	],
	entry_points='''
''')
```