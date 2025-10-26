Name:         count_files
Version:      1.0
Release:      1%{?dist}
Summary:      Script to count regular files in /etc
License:      GPL-3.0+
BuildArch:    noarch
Requires:     /bin/bash
Source0:      %{name}-%{version}.tar.gz

%description
This package installs a simple script that counts regular files
(excluding directories and symlinks) in the /etc directory.
It should be run as root.

%prep
%setup -q

%build
# Nothing to build

%install
rm -rf %{buildroot}
install -D -m 0755 count_files.sh %{buildroot}%{_bindir}/%{name}

%files
%license
%{_bindir}/%{name}

%changelog
* Sat Oct 26 2025 Mykhnevych Dmytro <grandmasterdima@gmail.com> - 1.0-1
- Initial RPM release with count_files.sh
