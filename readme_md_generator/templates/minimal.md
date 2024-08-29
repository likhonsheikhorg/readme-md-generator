/**
 * Likhon Sheikh 
 *
 * @author Likhon Sheikh <https://likhonsheikh.com>
 * @copyright 2023-2024 Likhon Sheikh
 * @mail  <me@likhonsheikh.com>
 * @telegram Likhon Sheikh  <https://t.me/likhondotxyz>
 */



# {{ name }}

{% if description %}
{{ description }}
{% endif %}

## Installation

```
{{ install if install else "npm install" }}
```

## Usage

```
{{ usage if usage else "npm start" }}
```

## Author

**{{ author }}**

* Website: {{ website }}
* GitHub: [@{{ github }}](https://github.com/{{ github }})

## License

{{ license }}

***
This README was generated with ❤️ by [readme-md-generator](https://github.com/likhonsheikhorg/readme-md-generator)
