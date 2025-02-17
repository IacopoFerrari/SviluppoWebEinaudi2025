Ci sono due account utente e un account admin, il primo account utente, ha nome utente "user" e password sconosciuta,
il secondo account utente ha nome utente "user2" e password "user2", l'account admin ha nome utente "admin" e
password "admin".
per loggarsi con un account bisogna fare una post all'endpoint "/login" e passargli json con chiavi "username" e
"password".
quando si è loggati con un account utente (non admin) è possibile accedere con una get all'endpoint "/secret_code",
il quale ritornerà un codice se si è loggati con l'utente 1, e un altro codice se si è loggati con l'utente 2.
Non conoscendo la password dell'utente 1 bisogna accedere con un account che abbia i permessi necessari per accedere, con
una post all'endpoint "change_password/" e passargli un json con chiavi "username":"username dell'utente per il quale
si vuole cambiare password" e "new_password":"nuova password che si vuole impostare per l'utente del parametro precedente".
L'obbiettivo è riuscire a fare una post all'endpoint "/check" e passargli un dizionario con chiave "code" e valore
la somma dei due codici, se ritorna codice corretto l'esercizio è completato.
