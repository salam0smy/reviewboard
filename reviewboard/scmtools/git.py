from reviewboard.scmtools import sshutils
sshutils.register_rbssh('GIT_SSH')

        super(GitTool, cls).check_repository(client.path, username, password)

        if self._is_newfile_or_deleted_change(linenum):
    def _is_newfile_or_deleted_change(self, linenum):
        return (line.startswith("new file mode")
                or line.startswith("deleted file mode"))
            p = self._run_git(['--git-dir=%s' % self.git_dir, 'config',
                               'core.repositoryformatversion'])
        p = self._run_git(['ls-remote', self.path, 'HEAD'])
    def _run_git(self, args):
        """Runs a git command, returning a subprocess.Popen."""
        return subprocess.Popen(
            ['git'] + args,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
            close_fds=(os.name != 'nt')
        )

        p = self._run_git(['--git-dir=%s' % self.git_dir, 'cat-file',
                           option, commit])