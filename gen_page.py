import os
import platform
import subprocess
import sys
import timeit

from jinja2 import Template
from unipath import Path, DIRS, FILES

NUMBER = 1000000

base_path = Path(os.path.abspath(__file__)).parent
dis_template = Path(base_path, 'dis_template.py').read_file()
template = Template(base_path.child('template.html').read_file())
test_path = Path(base_path, 'tests')
tmp = Path('/tmp')


def main():
    def gen_tests():
        for Tx, group_x_dir in enumerate(test_path.walk(filter=DIRS), 1):
            print "Gen Test: %s" % Tx
            group = []
            for tx, test_x_file in enumerate(group_x_dir.walk(filter=FILES), 1):
                print "    Sub Test: %s" % tx
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
                group.append({
                    'dis': out,
                    'file_content': file_content,
                    'number': number,
                    'timeit_min': min(timeit.repeat(f['a'], number=number)),
                })
            group.sort(key=lambda x: x['timeit_min'])

            yield {
                'n': Tx,
                'span': 12 / len(group),
                'cases': group,
            }

    ts = template.stream({
        'plat_sys': platform.system(),
        'plat_rel': platform.release(),
        'sys_version': sys.version,
        'tests': gen_tests()
    })
    ts.enable_buffering()
    ts.dump('index.html')


if __name__ == '__main__':
    main()
