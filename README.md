# episode-video-index-audit

## Français

Détecter les épisodes rattachés au mauvais fichier vidéo.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m episode_video_index_audit examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Vérifie les références vidéo, durées et bornes de frames depuis un manifeste exporté ; cite LeRobot5039 mais ne copie pas son stockage. Les alternatives sont seulement des candidats de longueur.

### Limites

Ne décode pas de vidéo et ne prouve pas le bon contenu visuel ; métadonnées fournies à vérifier, aucune réparation automatique.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Detect episodes assigned to the wrong video file.

Synthetic data; no network access or secret required.

```sh
python -m episode_video_index_audit examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Checks video references, durations and frame bounds from an exported manifest; motivated by LeRobot5039 without copying its storage. Alternatives are length-only candidates.

### Limits

Does not decode video or prove visual content correctness; supplied metadata require checking, no automatic repair.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Detectar episodios asignados al archivo de vídeo incorrecto.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m episode_video_index_audit examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Comprueba referencias de vídeo, duraciones y límites de frames desde manifiesto exportado; motivado por LeRobot5039 sin copiar almacenamiento. Alternativas solo por longitud.

### Límites

No decodifica vídeo ni prueba contenido visual correcto; verificar metadatos aportados, sin reparación automática.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://github.com/huggingface/lerobot/issues/5039
