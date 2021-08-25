# Legal Advice Demo
This is a demo project to allow a quickstart of the [Django Legal Advice Builder](https://github.com/OpenLegalTech/django-legal-advice-builder) and see how it works. For more information check the [Django Legal Advice Builder README](https://github.com/OpenLegalTech/django-legal-advice-builder#readme).

Be aware that this project is in German.

```
git clone git@github.com:OpenLegalTech/legal-advice-demo.git
cd legal-advice-demo
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd legal_advice_demo/
cp .env_sample  .env
./manage.py migrate
./manage.py runserver
```
browse to http://localhost:8000/

