# LaunchEazy MicrosoftOutlookAuthApp

## How to setup

1. Clone the repo
```bash
git clone https://github.com/siddhantdixit/MicrosoftOutlookAuthApp
```

2. Create virtual environement, (we recommend pipenv)
```bash
cd MicrosoftOutlookAuthApp
pipenv install
```


3. Add `aad.config.json` in the project directory which stores necessary details for your Azure App Credentials
```javascript
{
    "type": {
        "client_type": "CONFIDENTIAL",
        "authority_type": "SINGLE_TENANT",
        "framework": "DJANGO"
    },
    "client": {
        "client_id": <YOUR-CLIENT-ID>",
        "client_credential": "<YOUR-CLIENT-SECRET>",
        "authority": "https://login.microsoftonline.com/<YOUR-TENANT-ID>"
    },
    "auth_request": {
        "redirect_uri": null,
        "scopes": [],
        "response_type": "code"
    },
    "flask": null,
    "django": {
        "id_web_configs": "MS_ID_WEB_CONFIGS",
        "auth_endpoints": {
            "prefix": "auth",
            "sign_in": "sign_in",
            "edit_profile": "edit_profile",
            "redirect": "redirect",
            "sign_out": "sign_out",
            "post_sign_out": "post_sign_out"
        }
    }
}
```


5. Use the below commands to setup django project

```
python manage.py collectstatic
python manage.py migrate
python manage.py runserver localhost:8000
```


## Images
![image](https://github.com/siddhantdixit/MicrosoftOutlookAuthApp/assets/22856752/bba3011a-fbec-450a-9100-f78bcf5f1471)

![image](https://github.com/siddhantdixit/MicrosoftOutlookAuthApp/assets/22856752/b0eec405-a656-47c0-a717-f62f60a2f2cb)


![image](https://github.com/siddhantdixit/MicrosoftOutlookAuthApp/assets/22856752/865d0f77-2000-4daa-a4a7-758b46daca4e)

![image](https://github.com/siddhantdixit/MicrosoftOutlookAuthApp/assets/22856752/2bf0b348-e7e2-4e20-b5f3-200fef407bad)
