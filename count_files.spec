Name:         count_files
Version:      1.0
Release:      1
Summary:      Script to count regular files in /etc
License:      GPL-3.0+
BuildArch:    noarch
Requires:     /bin/bash
Source0:      count_files-1.0.tar.gz


%description
This package installs a simple script that counts regular files
(excluding directories and symlinks) in the /etc directory.
It should be run as root.

%clean
%{__rm} -rf %{buildroot}

%prep
%setup -q

%build

%install
install -D -m 0755 script.sh %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}


%changelog
* Thu Oct 25 2025 Mykhnevych Dmytro <grandmasterdima@gmail.com> - 1.0-1
- Initial RPM release with count_files.sh
