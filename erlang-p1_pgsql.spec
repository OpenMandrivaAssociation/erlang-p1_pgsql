%global realname p1_pgsql
%global upstream processone
# Technically, we're noarch; but erlang whose directories we install into is not.
%global debug_package %{nil}


Name:       erlang-%{realname}
Version:    1.1.0
Release:    %mkrel 1
Provides:   erlang-pgsql = %{version}-%{release}
Obsoletes:  erlang-pgsql < 0-16
Summary:    Pure Erlang PostgreSQL driver
Group:      Development/Erlang
License:    ERPL
URL:		https://github.com/%{upstream}/%{realname}
%if 0%{?el7}%{?fedora}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
%endif
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
# A Fedora-specific patch which restores API from erlang-pgsql package thus
# allowing fully seamless transition
Patch1:     erlang-p1_pgsql-0001-Restore-old-API.patch

BuildRequires: erlang-rebar

%description
Pure Erlang PostgreSQL driver.

%prep
%autosetup -n %{realname}-%{version} -p1

%build
%{erlang_compile}

%check 
%__rebar eunit

%install
%{erlang_install}

%files
%doc README.md
%license EPLICENSE
%{erlang_appdir}/



%changelog
* Thu Nov 17 2016 neoclust <neoclust> 1.1.0-1.mga6
+ Revision: 1068059
- New version 1.1.0

* Fri May 06 2016 neoclust <neoclust> 1.0.0-1.mga6
+ Revision: 1009914
- imported package erlang-p1_pgsql

