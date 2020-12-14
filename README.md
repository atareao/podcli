
<!-- start project-info -->
<!--
project_title: podcli
github_project: https://github.com/atareao/podcli
license: MIT
icon: /datos/Sync/Programacion/Python/podcli/data/icons/podcli.svg
homepage: https://www.atareao.es/aplicacion/podcli
license-badge: True
contributors-badge: True
lastcommit-badge: True
codefactor-badge: True
--->

<!-- end project-info -->

<!-- start badges -->

![License MIT](https://img.shields.io/badge/license-MIT-green)
![Contributors](https://img.shields.io/github/contributors-anon/atareao/podcli)
![Last commit](https://img.shields.io/github/last-commit/atareao/podcli)
[![CodeFactor](https://www.codefactor.io/repository/github/atareao/podcli/badge/master)](https://www.codefactor.io/repository/github/atareao/podcli/overview/master)
<!-- end badges -->

<!-- start description -->
<h1 align="center">Welcome to <span id="project_title">podcli</span> 👋</h1>
<p>
<a href="https://www.atareao.es/aplicacion/podcli" id="homepage" rel="nofollow">
<img align="right" height="128" id="icon" src="data/icons/podcli.svg" width="128"/>
</a>
</p>
<h2>🏠 <a href="https://www.atareao.es/aplicacion/podcli" id="homepage">Homepage</a></h2>
<p><span id="project_title">podcli</span> is a simple application to download podcast from RSS.

</p>
<!-- end description -->

<!-- start prerequisites -->
## Prerequisites

Before you begin, ensure you have met the following requirements:

* If you install it from PPA don't worry about, becouse all the requirements are included in the package
* If you clone the repository, you need, at least, these dependecies,

```
gir1.2-gtk-3.0
gir1.2-glib-2.0
gir1.2-gdkpixbuf-2.0
gir1.2-appindicator3-0.1
gir1.2-keybinder-3.0
```


<!-- end prerequisites -->

<!-- start installing -->
## Installing <span id="project_title">podcli</span>

To install <span id="project_title">podcli</span>, follow these steps:

* In a terminal (`Ctrl+Alt+T`), run these commands

```
sudo add-apt-repository ppa:atareao/atareao
sudo apt update
sudo apt install podcli
```



<!-- end installing -->

<!-- start using -->
## Using <span id="project_title">podcli</span>

```
usage: podcli [-h] [-a] [-b] [-d] [-e] [-f FIRST] [-i] [-l LAST] [-p] [-s] -u
              URL

Podcast parser

optional arguments:
  -h, --help            show this help message and exit
  -a, --audio           Descargando audio
  -b, --debug           Solo para depuración
  -d, --docs            Muestra el contenido del episodio en formato html
  -e, --enumerate       Lista los episodios
  -f FIRST, --first FIRST
                        Selecciona el primer episodio
  -i, --images          Descarga imágenes
  -l LAST, --last LAST  Selecciona el primer episodio
  -p, --play            Reproduce el audio y lo descarga si es necesario
  -s, --show            Muestra el contenido del episodio en formato markdown
  -u URL, --url URL     La url o el nombre del archivo del feed

```


<!-- end using -->

<!-- start contributing -->
## Contributing to <span id="project_title">podcli</span>

To contribute to **<span id="project_title">podcli</span>**, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin atareao/podcli`
5. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).
</commit_message></branch_name>

<!-- end contributing -->

<!-- start contributors -->
## 👤 Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):


<!-- end contributors -->

<!-- start table-contributors -->

<table id="contributors">
	<tr id="info_avatar">
		<td id="atareao" align="center">
			<a href="https://github.com/atareao">
				<img src="https://avatars3.githubusercontent.com/u/298055?v=4" width="100px"/>
			</a>
		</td>
	</tr>
	<tr id="info_name">
		<td id="atareao" align="center">
			<a href="https://github.com/atareao">
				<strong>Lorenzo Carbonell</strong>
			</a>
		</td>
	</tr>
	<tr id="info_commit">
		<td id="atareao" align="center">
			<a href="/commits?author=atareao">
				<span id="role">💻</span>
			</a>
		</td>
	</tr>
</table>
<!-- end table-contributors -->
