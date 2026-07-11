%global tl_name drawmatrix
%global tl_revision 44471

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5.0
Release:	%{tl_revision}.1
Summary:	Draw visual representations of matrices in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/drawmatrix
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/drawmatrix.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/drawmatrix.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/drawmatrix.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides macros to visually represent matrices. Various
options allow to change the visualizations, e.g., drawing rectangular,
triangular, or banded matrices.

