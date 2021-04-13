# wikitrad

## Installation

_wikitrad_ is available [on PyPI](https://pypi.org/project/wikitrad):

```sh
pip install wikitrad
```

### Arch Linux

Arch users can install it from [the AUR](https://aur.archlinux.org/packages/wikitrad)

```sh
paru wikitrad # or any AUR helper
```

You can also get a bleeding edge release with [_wikitrad-git_](https://aur.archlinux.org/packages/wikitrad-git).

## Usage

Language codes refer to the language codes used by wikipedia: `en` for `en.wikipedia.org`, `fr` for `fr.wikipedia.org`, etc.

### Without specifying the source language

```sh
wikitrad "word to translate" target_language_code
```
### specifying the source language

```sh
wikitrad source_language_code "word to translate" target_language_code
```

