from muslang.scanner import scan


success = '''module Success end

let C-major-3 = merge C-3 E-3 G-3 end

let D-minor-3 = merge D-3 F-3 A-4 end

let prog = progression C-major-3 D-minor-3 C-major-3 C-major-3 D-minor-3 end

compose prog end'''

print(success)

success_module_str = [
    ('keyword', 'module'),
    ('identifier', 'Success'),
    ('keyword', 'end')
]

success_c_major_3 = [
    ('keyword', 'let'),
    ('identifier', 'C-major-3'),
    ('operator', '='),
    ('keyword', 'merge'),
    ('note', 'C-3'),
    ('note', 'E-3'),
    ('note', 'G-3'),
    ('keyword', 'end')
]

success_d_minor_3 = [
    ('keyword', 'let'),
    ('identifier', 'D-minor-3'),
    ('operator', '='),
    ('keyword', 'merge'),
    ('note', 'D-3'),
    ('note', 'F-3'),
    ('note', 'A-4'),
    ('keyword', 'end')
]

success_progression = [
    ('keyword', 'let'),
    ('identifier', 'progression'),
    ('operator', '='),
    ('keyword', 'progression'),
    ('identifier', 'C-major-3'),
    ('identifier', 'D-minor-3'),
    ('identifier', 'C-major-3'),
    ('identifier', 'C-major-3'),
    ('identifier', 'D-minor-3')
]

success_compose = [
    ('keyword', 'produce'),
    ('identifier', 'prog'),
    ('keyword', 'end')
]

def test_scan_success():
    statements = scan(success)
    module = statements[0]
    for a, b in zip(module, success_module_str):
        assert a.descriptor() == b
