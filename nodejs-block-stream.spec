%define		pkg	block-stream
Summary:	A stream of blocks
Name:		nodejs-%{pkg}
Version:	0.0.5
Release:	1
License:	MIT
Group:		Development/Libraries
URL:		https://github.com/isaacs/block-stream
Source0:	http://registry.npmjs.org/%{pkg}/-/%{pkg}-%{version}.tgz
# Source0-md5:	f70aecb5466ca512c67c5a3a8e74096e
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
Requires:	nodejs-inherits >= 1.0.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A stream of blocks.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -pr %{pkg}.js package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{nodejs_libdir}/%{pkg}
