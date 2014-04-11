import os
import platform
import subprocess
import sys

from jinja2 import Template
from timeit import timeit
from unipath import Path, DIRS, FILES

TESTS = []
NUMBER = 1000000

base_path = Path(os.path.abspath(__file__)).parent
dis_template = Path(base_path, 'dis_template.py').read_file()
template = Template(base_path.child('template.html').read_file())
test_path = Path(base_path, 'tests')
tmp = Path('/tmp')


def main():

    for group_x_dir in test_path.walk(filter=DIRS):
        group = []
        TESTS.append(group)
        for test_x_file in group_x_dir.walk(filter=FILES):
            file_content = test_x_file.read_file()

            dis_test_content = dis_template % file_content

            dis_test_file = tmp.child('__pfw_%s_%s' % (group_x_dir.name, test_x_file.name))
            dis_test_file.write_file(dis_test_content)

            p = subprocess.Popen(
                ['python', '-B', str(dis_test_file)],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            out, err = p.communicate()

            dis_test_file.remove()

            code = compile(file_content, '<string>', 'exec')

            f = {'number': None}
            exec code in f
            number = f['number'] or NUMBER
            dic = {
                'dis': out,
                'file_content': file_content,
                'number': number,
                'timeit': timeit(f['a'], number=number),
            }
            group.append(dic)
        group.sort(key=lambda x: x['timeit'])

    context = {
        'plat_sys': platform.system(),
        'plat_rel': platform.release(),
        'sys_version': sys.version,
        'tests': [
            {
                'n': k + 1,
                'span': 12 / len(v),
                'cases': v,
            }
            for k, v in enumerate(TESTS)
        ]
    }

    print template.render(context)


if __name__ == '__main__':
    main()
