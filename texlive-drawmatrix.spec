Name:		texlive-drawmatrix
Version:	44471
Release:	2
Summary:	Draw visual representations of matrices in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/drawmatrix
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/drawmatrix.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/drawmatrix.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/drawmatrix.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides macros to visually represent matrices.
Various options allow to change the visualizations, e.g.,
drawing rectangular, triangular, or banded matrices.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/drawmatrix
%{_texmfdistdir}/tex/latex/drawmatrix
%doc %{_texmfdistdir}/doc/latex/drawmatrix

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
