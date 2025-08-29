```bash
docker build -t ai .
```
python REPL
```bash
docker run --rm -it --name ai-server ai
```

ファイルをマウントしてコンテナに入る
```
docker run --rm -v ./:/var/app -it --name ai-server ai /bin/bash
```