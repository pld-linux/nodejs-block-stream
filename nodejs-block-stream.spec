%define		pkg	block-stream
Summary:	A stream of blocks
Name:		nodejs-%{pkg}
Version:	0.0.7
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	http://registry.npmjs.org/%{pkg}/-/%{pkg}-%{version}.tgz
# Source0-md5:	c66aaa2227abec6daa6ff8a155b59294
URL:		https://github.com/isaacs/block-stream
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs >= 0.5.8
Requires:	nodejs-inherits < 3.0.0
Requires:	nodejs-inherits >= 2.0.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A stream of blocks. Write data into it, and it'll output data in
buffer blocks the size you specify, padding with zeroes if necessary.

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
