run: dev
	build/hotreload.dev.exe

dev: build
	gcc -O1 -Wall -Wextra src/main.c -o build/hotreload.dev.exe

prod: build
	gcc -O3 -Wall -Wextra src/main.c -o build/hotreload.exe

build:
	mkdir build
