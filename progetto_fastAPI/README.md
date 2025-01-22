# GUIDA AL SET UP

## Cosa fare appena si esegue la pull da github

Appena fatta la pull da github svolgere i seguenti comandi nella directory `progetto_fastAPI/` per installare il venv:

```bash
python3 -m venv venv
```

questo installerà l'ambiente virtuale nella cartella venv.
Una volta installato il venv eseguire questo comando 
attivare l'ambiente virtuale (a.k.a. venv) e infine esegui:

```bash
#su Windows
venv\Scripts\activate

#su MacOS o Linux
source venv/bin/activate
```

per installare tutte le librerie:
pip install -r requirements.txt

Per uscire dall'ambiente virtuale si utilizza il comando:

```bash
deactivate
```

## Come avviare l'applicazione

Per avviare l'applicazione bisogna entrare nell'ambiente virutale con il comando sopra ed eseguire il seguente comando:

```bash
uvicorn main:app --reload
```



Ad ogni salvataggio dei file del backend il programma si riavvia da solo se il parametro `--reload` è presente. In caso abbia avviato il programma con il secondo comando bisogna chiudere con `Ctrl+C` il programma e riavviarlo con lo stesso comando con cui è stato avviato in precedenza.

L'applicazione è hostata su [http://localhost:8000](http://localhost:8000) ma per utilizzare gli endpoint bisogna accederci tramite postman che in caso è possibile scaricare [qui](https://www.postman.com/downloads/).

## Cosa fare quando si aggiungono nuove librerie

Quanto si aggiungono delle nuove librerie nei file di questa directory bisogna eseguire il seguente comando dopo aver attivato l'ambiente virtuale con il comando eseguito in precedenza:

```bash
pip freeze > requirements.txt
```

## Cosa fare quando le librerie installate non sono aggiornate

Quando, dopo una pull, mandando in esecuzione il backend dice che mancano delle librerie bisogna lanciare il seguente comando, sempre dopo aver attivato l'ambiente virtuale con il comando scritto sopra:

```bash
pip install --upgrade -r requirements.txt
```

## Documentazione FastAPI

Se avete bisogno della documentazione di FastApi consultate questo [link](https://fastapi.tiangolo.com/lo/).