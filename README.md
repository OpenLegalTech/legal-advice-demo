# legal-advice-demo

```
git clone git@github.com:OpenLegalTech/legal-advice-demo.git
cd legal-advice-demo
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd legal_advice_demo/
cp .env_sample  .env
./manage.py migrate
./manage.py loaddata ./fixtures/sample_data.json
./manage.py runserver
browse to http://localhost:8000/advicebuilder/admin/
```
