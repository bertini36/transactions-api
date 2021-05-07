# bertini36/transactions-api 💰
Small API that allows to register transactions in order to obtain account
balances.

## 🚀 Environment Setup

### 🐳 Required tools

1. [Install Docker and Docker Compose](https://www.docker.com/get-started)
2. Clone this project: `git clone https://github.com/bertini36/transactions-api`
3. Move to the project folder: `transactions-api`

### 🔥 Application execution

* Install all the dependencies: `make build`
* Create the database: `make migrate`
* Run the server: `make up`

### Transactions registration

* `make load-transactions-csv [args="--csv-file 'path/to/file.csv'"]`
or from
* http://127.0.0.1/admin/transactions/uploadedcsvfile/add/

### Transactions queries
TODO

### ✅ Tests execution

- Run tests: `make tests`

### 🤔 Extra commands 

- Check `Makefile` to know all available commands 

<p align="center">&mdash; Built with :heart: from Mallorca &mdash;</p>
