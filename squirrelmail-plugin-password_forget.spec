%define		_plugin	password_forget
%define		mversion	1.0.1
Summary:	Plugin for login/password form names randomization
Summary(pl):	Wtyczka generuj±ca losowe nazwy pól login/has³o w formularzu
Name:		squirrelmail-plugin-%{_plugin}
Version:	2.1
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://www.squirrelmail.org/plugins/%{_plugin}.%{version}-%{mversion}.tar.gz
# Source0-md5:	33ffd387d5190b690d53358cb3b4e691
URL:		http://www.squirrelmail.org/
Requires:	squirrelmail >= 1.4.6-2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%{_datadir}/squirrelmail/plugins/%{_plugin}
%define		_sysconfdir	/etc/webapps/squirrelmail

%description
This plugin will generate random names for login/password form fields
to prevent browsers for remembering users passwords.

%description -l pl
Ta wtyczka bêdzie generowaæ losowe nazwy pól formularza dla loginu i
has³a aby uniemo¿liwiæ przegl±darkom zapamiêtywanie hase³
u¿ytkowników.

%prep
%setup -q -n %{_plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_plugindir} $RPM_BUILD_ROOT%{_sysconfdir}

install *.php $RPM_BUILD_ROOT%{_plugindir}
mv config.php.sample $RPM_BUILD_ROOT%{_sysconfdir}/%{_plugin}_config.php
ln -s %{_sysconfdir}/%{_plugin}_config.php $RPM_BUILD_ROOT%{_plugindir}/config.php

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL README
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{_plugin}_config.php
%dir %{_plugindir}
%{_plugindir}/*.php
