%global tl_name thesis-titlepage-fhac
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Little style to create a standard titlepage for diploma thesis
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/thesis-titlepage-fhAC
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/thesis-titlepage-fhac.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/thesis-titlepage-fhac.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/thesis-titlepage-fhac.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Yet another thesis titlepage style: support of Fachhochschule Aachen
(Standort Juelich)

