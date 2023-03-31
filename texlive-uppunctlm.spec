Name:		texlive-uppunctlm
Version:	42334
Release:	2
Summary:	Always keep upright shape for some punctuation marks and Arabic numerals
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/uppunctlm
License:	gfsl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uppunctlm.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uppunctlm.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a mechanism to keep punctuation always in
upright shape even if italic was specified. It is directed to
Latin Modern fonts, and provides .tfm, .vf, .fd, and .sty
files. Here a list of punctuation characters always presented
in upright shapes: comma, period, semicolon, colon,
parentheses, square brackets, and Arabic numerals.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/uppunctlm
%{_texmfdistdir}/fonts/vf/public/uppunctlm
%{_texmfdistdir}/fonts/tfm/public/uppunctlm
%doc %{_texmfdistdir}/doc/fonts/uppunctlm

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
