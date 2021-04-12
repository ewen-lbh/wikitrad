# Maintainer: Ewen Le Bihan <hey@ewen.works>

pkgname=wikitrad-git
pkgver=0.2.0
pkgrel=1
pkgdesc="A CLI to translate terms with wikipedia"
#epoch=0
arch=('any')
url="https://github.com/ewen-lbh/wikitrad"
license=('GPL')
depends=('python')
makedepends=('git', 'pip')
provides=('wikitrad')
source=(http://server/$pkgname-$pkgver.tar.gz)
md5sums=('SKIP')

source=("git+https://github.com/ewen-lbh/wikitrad.git")

pkgver() {
  cd $pkgname
  cat pyproject.toml | grep "version" | head -1 | cut -d '"' -f 2
}

package() {
  pip install $pkgname --root="${pkgdir}" --prefix=/usr
}

# vim:set ts=2 sw=2 et:

