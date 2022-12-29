build:
	/usr/bin/python3 /Users/sherm/Library/Python/3.9/lib/python/site-packages/pyinstaller main.spec

run: build
	./dist/main/my_exe -l 
	./dist/main/my_exe -h

clean:
	rm -rf dist build
