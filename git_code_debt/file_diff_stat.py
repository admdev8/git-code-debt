from __future__ import absolute_import
from __future__ import unicode_literals
# pylint:disable=too-many-branches,too-many-statements


    BINARY = object()
        'FileDiffStat',
        ['path', 'lines_added', 'lines_removed', 'status', 'special_file'],
SUBMODULE_MODE = b'160000'
SYMLINK_MODE = b'120000'
    lines = file_diff.split(b'\n')
    diff_line_filename = lines[0].split()[-1].lstrip(b'b').lstrip(b'/')
    is_binary = False
        if line.startswith(b'new file mode '):
        elif line.startswith(b'deleted file mode '):
        elif line.startswith(b'new mode '):
        elif line.startswith(b'index') and len(line.split()) == 3:
        elif line.startswith(b'Binary files'):
            is_binary = True
        elif line.startswith(b'--- ') and not in_diff:
            pass
        elif line.startswith(b'+++ ') and not in_diff:
        elif in_diff and line.startswith(b'+'):
        elif in_diff and line.startswith(b'-'):
    elif is_binary:
        special_file = SpecialFile(
            file_type=SpecialFileType.BINARY,
            added=diff_line_filename if status is not Status.DELETED else None,
            removed=diff_line_filename if status is not Status.ADDED else None,
        )
GIT_DIFF_RE = re.compile(b'^diff --git', flags=re.MULTILINE)
    assert type(output) is bytes, (type(output), output)
    assert not files[0].strip() or files[0].startswith(b'commit ')
    return [_to_file_diff_stat(file_diff) for file_diff in files[1:]]