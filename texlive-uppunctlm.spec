%global tl_name uppunctlm
%global tl_revision 42334

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Always keep upright shape for some punctuation marks and Arabic numerals
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/uppunctlm
License:	gfsl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uppunctlm.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uppunctlm.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a mechanism to keep punctuation always in upright
shape even if italic was specified. It is directed to Latin Modern
fonts, and provides .tfm, .vf, .fd, and .sty files. Here a list of
punctuation characters always presented in upright shapes: comma,
period, semicolon, colon, parentheses, square brackets, and Arabic
numerals.

