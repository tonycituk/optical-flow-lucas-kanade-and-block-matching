# optical-flow-lucas-kanade-and-block-matching

### Crear Ambiente Python

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Generar imágenes I_k-1 e I_k

```bash
python src/generateImages.py
```

| I_k-1 | I_k |
|---|---|
| [![I_k-1](src/resources/I_k-1.png)](src/resources/I_k-1.png) | [![I_k](src/resources/I_k.png)](src/resources/I_k.png) |