import AST


def plus(larg, rarg):
    return larg + rarg


def sub(larg, rarg):
    return larg - rarg


def mul(larg, rarg):
    return larg * rarg


def div(larg, rarg):
    return larg / rarg


def neg(arg):
    if isinstance(arg, AST.Matrix):
        for row in arg.rows:
            row_length = len(row.row)
            for i in range(row_length):
                row.row[i] = -row.row[i]
        return arg
    else:
        return -arg


def trans(arg):
    ret = AST.Matrix(arg.line)
    row_size = len(arg.rows)
    for i in range(row_size):
        ret.add_row(AST.MatrixRow(arg.line))
    for i in range(row_size):
        for j in range(row_size):
            ret.rows[j].add_elem(arg.rows[i].row[j])
    return ret


def dot_plus(larg, rarg):
    ret = AST.Matrix(larg.line)
    row_size = len(larg.rows)
    for i in range(row_size):
        ret.add_row(AST.MatrixRow(larg.line))
    for i in range(row_size):
        for j in range(row_size):
            ret.rows[i].row[j] = larg.rows[i].row[j] + rarg.rows[i].row[j]
    return ret


def dot_sub(larg, rarg):
    ret = AST.Matrix(larg.line)
    row_size = len(larg.rows)
    for i in range(row_size):
        ret.add_row(AST.MatrixRow(larg.line))
    for i in range(row_size):
        for j in range(row_size):
            ret.rows[i].row[j] = larg.rows[i].row[j] - rarg.rows[i].row[j]
    return ret


def dot_mul(larg, rarg):
    ret = AST.Matrix(larg.line)
    row_size = len(larg.rows)
    for i in range(row_size):
        ret.add_row(AST.MatrixRow(larg.line))
    for i in range(row_size):
        for j in range(row_size):
            ret.rows[i].row[j] = larg.rows[i].row[j] * rarg.rows[i].row[j]
    return ret


def dot_div(larg, rarg):
    ret = AST.Matrix(larg.line)
    row_size = len(larg.rows)
    for i in range(row_size):
        ret.add_row(AST.MatrixRow(larg.line))
    for i in range(row_size):
        for j in range(row_size):
            ret.rows[i].row[j] = larg.rows[i].row[j] / rarg.rows[i].row[j]
    return ret
