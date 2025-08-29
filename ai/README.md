```bash
docker build -t ai .
```
python REPL
```bash
docker run --rm -it --name ai-server ai
```

ファイルをマウントしてコンテナに入る
```bash
docker run --rm -v ./:/var/app -it --name ai-server ai /bin/bash
```

```bash
docker run --rm -v ./:/var/app -p 8000:8000 --name ai-server -e OPENAI_API_KEY='your_actual_api_key' ai
```

```bash
curl -X POST http://localhost:8000/chat -H "Content-Type: application/json" -d '{"message": "こんにちは、ビールジョッキ何杯までなら健康的でしょうか？", "temperature": 0.7}'
```