# bertini36/transactions-api 💰
Small API that allows to register transactions in order to obtain account
balances.

Statement: https://github.com/abacum-io/abacum-recruitment-test/blob/master/backed-python/test-python-backend-engineer.md

## 🚀 Environment Setup

### 🐳 Required tools

1. [Install Docker and Docker Compose](https://www.docker.com/get-started)
2. Clone this project: `git clone https://github.com/bertini36/transactions-api`
3. Move to the project folder: `transactions-api`

### 🔥 Application execution

* Install all the dependencies: `make build`
* Create the database: `make migrate`
* Create user: `make createsuperuser`
* Run the server: `make up`

### Transactions registration

* `make load-transactions-csv [args="--csv-file 'path/to/file.csv'"]`
or from
* http://127.0.0.1/admin/transactions/uploadedcsvfile/add/

### Transactions queries

* Get a full year balance by account: http://127.0.0.1/annual/balances/all/2020/
* Get a full year balance for a specific account: http://127.0.0.1/annual/balances/10000000/2020/
* Get monthly balances by account: http://127.0.0.1/monthly/balances/all/
* Get monthly balance for a specific account: http://127.0.0.1/monthly/balances/10000000/
* Get the monthly balance for a specific month by account: http://127.0.0.1/monthly/balances/10000000/2020/3/

### ✅ Tests execution

- Run tests: `make tests`

### 🔦 Lint

- Run lint: `make lint`

### 🤔 Extra commands 

- Check `Makefile` to know all available commands 

<p align="center">&mdash; Built with :heart: from Mallorca &mdash;</p>
