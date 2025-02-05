### Frappe Msdoc Template

Generate documents from MS Docs templates

[Please, see Wiki](https://github.com/rareMaxim/frappe_msdoc_template/wiki)

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app https://github.com/rareMaxim/frappe_msdoc_template --branch develop
bench install-app frappe_msdoc_template
```


### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/frappe_msdoc_template
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### License

mit
