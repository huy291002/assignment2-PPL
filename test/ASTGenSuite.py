import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
# #     def test_short_vardecl(self):
# #         input = """x: integer;"""
# #         expect = str(Program([VarDecl("x", IntegerType())]))
# #         self.assertTrue(TestAST.test(input, expect, 300))

# #     def test_full_vardecl(self):
# #         input = """x, y, z: integer = 1, 2, 3;"""
# #         expect = """Program([
# # 	VarDecl(x, IntegerType, IntegerLit(1))
# # 	VarDecl(y, IntegerType, IntegerLit(2))
# # 	VarDecl(z, IntegerType, IntegerLit(3))
# # ])"""         
# #         self.assertTrue(TestAST.test(input, expect, 301))

# #     def test_vardecls(self):
# #         input = """x, y, z: integer = 1, 2, 3;
# #         a, b: float;"""
# #         expect = """Program([
# # 	VarDecl(x, IntegerType, IntegerLit(1))
# # 	VarDecl(y, IntegerType, IntegerLit(2))
# # 	VarDecl(z, IntegerType, IntegerLit(3))
# # 	VarDecl(a, FloatType)
# # 	VarDecl(b, FloatType)
# # ])"""
# #         self.assertTrue(TestAST.test(input, expect, 302))

# #     def test_simple_program(self):
# #         """Simple program"""
# #         input = """main: function void () {
# #         }"""
# #         expect = """Program([
# # 	FuncDecl(main, VoidType, [], None, BlockStmt([]))
# # ])"""
# #         self.assertTrue(TestAST.test(input, expect, 303))

#     def test_1(self):
#         """test 1"""
#         input = """h,c,d: boolean = true, false, true; """
#         expect = """Program([\n\tVarDecl(h, BooleanType, BooleanLit(True))\n\tVarDecl(c, BooleanType, BooleanLit(False))\n\tVarDecl(d, BooleanType, BooleanLit(True))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 301))

#     def test_2(self):
#         """test 2"""
#         input = """l,h,q,f,g: integer = 1_23_54_29, 2482_29, 1.2e+4, quan, false; """
#         expect = """Program([\n\tVarDecl(l, IntegerType, IntegerLit(1235429))\n\tVarDecl(h, IntegerType, IntegerLit(248229))\n\tVarDecl(q, IntegerType, FloatLit(12000.0))\n\tVarDecl(f, IntegerType, Id(quan))\n\tVarDecl(g, IntegerType, BooleanLit(False))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 302))
#     def test_3(self):
#         """test 3"""
#         input = """h: array [2,3] of integer;q: string = "huy"; """
#         expect = """Program([\n\tVarDecl(h, ArrayType([2, 3], IntegerType))\n\tVarDecl(q, StringType, StringLit(huy))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 303))
#     def test_4(self):
#         """test 4"""
#         input = """huy, messi: integer = huy[2,9], quan[2,7]; """
#         expect = """Program([\n\tVarDecl(huy, IntegerType, ArrayCell(huy, [IntegerLit(2), IntegerLit(9)]))\n\tVarDecl(messi, IntegerType, ArrayCell(quan, [IntegerLit(2), IntegerLit(7)]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 304))
#     def test_5(self):
#         """test 5"""
#         input = """huy, goo, boo: string = "huy dang test \\n", "co gang lay diem cao \\b", "I lost her "; /* day chi la test */"""
#         expect = """Program([\n\tVarDecl(huy, StringType, StringLit(huy dang test \\n))\n\tVarDecl(goo, StringType, StringLit(co gang lay diem cao \\b))\n\tVarDecl(boo, StringType, StringLit(I lost her ))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 305))
#     def test_6(self):
#         """test 6"""
#         input = """huy, goo, boo: string = "huy dang test \\"xin dung lam phien \\r\\"\\n", _huy[1_0_12, 2_9], a[2, 7]; // dang alm test case"""
#         expect = """Program([\n\tVarDecl(huy, StringType, StringLit(huy dang test \\"xin dung lam phien \\r\\"\\n))\n\tVarDecl(goo, StringType, ArrayCell(_huy, [IntegerLit(1012), IntegerLit(29)]))\n\tVarDecl(boo, StringType, ArrayCell(a, [IntegerLit(2), IntegerLit(7)]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 306))
#     def test_7(self):
#         """test 7"""
#         input = """mami, baba, ache: float = _p_huong, 4_06_03_290, {3, 9}; // dang alm test case"""
#         expect = """Program([\n\tVarDecl(mami, FloatType, Id(_p_huong))\n\tVarDecl(baba, FloatType, IntegerLit(40603290))\n\tVarDecl(ache, FloatType, ArrayLit([IntegerLit(3), IntegerLit(9)]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 307))
#     def test_8(self):
#         """test 8"""
#         input = """qh_uy, _lost, __quan: boolean = true,true, {3_0_2_12, 23_1_0_123_4};"""
#         expect = """Program([\n\tVarDecl(qh_uy, BooleanType, BooleanLit(True))\n\tVarDecl(_lost, BooleanType, BooleanLit(True))\n\tVarDecl(__quan, BooleanType, ArrayLit([IntegerLit(30212), IntegerLit(23101234)]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 308))
#     def test_9(self):
#         """test 9"""
#         input = """h_uy_1_2, _goo_1, th_anh_0101: float = 29_10.2100, _h_uy[2_92, 9_01], {9_10, 2_1_12_90} ;
#                     a_bc_d, d_huy: string ;"""
#         expect = """Program([\n\tVarDecl(h_uy_1_2, FloatType, FloatLit(2910.21))\n\tVarDecl(_goo_1, FloatType, ArrayCell(_h_uy, [IntegerLit(292), IntegerLit(901)]))\n\tVarDecl(th_anh_0101, FloatType, ArrayLit([IntegerLit(910), IntegerLit(211290)]))\n\tVarDecl(a_bc_d, StringType)\n\tVarDecl(d_huy, StringType)\n])"""
#         self.assertTrue(TestAST.test(input, expect, 309))
#     def test_10(self):
#         """test 10"""
#         input = """h_uy_1_2: array [1_09, 2_9_1_0, 11_22_3_3] of string;
#                     a_bc_d29 : string = {"quan", "huy","thanh", "cuong"} ;
#                     t_quan_anh: float = {12.e+10, 1_2.10, 29_10.e3}; """
#         expect = """Program([\n\tVarDecl(h_uy_1_2, ArrayType([109, 2910, 112233], StringType))\n\tVarDecl(a_bc_d29, StringType, ArrayLit([StringLit(quan), StringLit(huy), StringLit(thanh), StringLit(cuong)]))\n\tVarDecl(t_quan_anh, FloatType, ArrayLit([FloatLit(120000000000.0), FloatLit(12.1), FloatLit(2910000.0)]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 310))
#     def test_11(self):
#         """test 11"""
#         input = """___lost_her: array [1_09, 2_11, 12_22] of boolean = a_29[19_1_20, "hello quan \\"quan khoe khong\\"", true, false, 1_27.21, 29_01];
#                     i__lost_u : auto = {12_21, "huy dang lam bai", false, 1.e-1} ;
#                     _huy_lost: float = {12.e+10, "huy lam bai \\f"}; """
#         expect = """Program([\n\tVarDecl(___lost_her, ArrayType([109, 211, 1222], BooleanType), ArrayCell(a_29, [IntegerLit(19120), StringLit(hello quan \\"quan khoe khong\\"), BooleanLit(True), BooleanLit(False), FloatLit(127.21), IntegerLit(2901)]))\n\tVarDecl(i__lost_u, AutoType, ArrayLit([IntegerLit(1221), StringLit(huy dang lam bai), BooleanLit(False), FloatLit(0.1)]))\n\tVarDecl(_huy_lost, FloatType, ArrayLit([FloatLit(120000000000.0), StringLit(huy lam bai \\f)]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 311))
#     def test_12(self):
#         """test 12"""
#         input = """___lost_her, a_29_10, d_1_01: integer = foo(2+x, 4/y), a+10/2, b_102 || 29 ; """
#         expect = """Program([\n\tVarDecl(___lost_her, IntegerType, FuncCall(foo, [BinExpr(+, IntegerLit(2), Id(x)), BinExpr(/, IntegerLit(4), Id(y))]))\n\tVarDecl(a_29_10, IntegerType, BinExpr(+, Id(a), BinExpr(/, IntegerLit(10), IntegerLit(2))))\n\tVarDecl(d_1_01, IntegerType, BinExpr(||, Id(b_102), IntegerLit(29)))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 312))
#     def test_13(self):
#         """test 13"""
#         input = """_quan, ___, huy_29: auto = m_12_01(2_123_1::x), !1.e1, -2_12e-2 ; """
#         expect = """Program([\n\tVarDecl(_quan, AutoType, FuncCall(m_12_01, [BinExpr(::, IntegerLit(21231), Id(x))]))\n\tVarDecl(___, AutoType, UnExpr(!, FloatLit(10.0)))\n\tVarDecl(huy_29, AutoType, UnExpr(-, FloatLit(2.12)))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 313))
#     def test_14(self):
#         """test 14"""
#         input = """_huy_29_n, __29_ : array [4_1_0_1] of string  = "quan \\b" != "huy \\f", 3_1_1_12_123 > 4_12_3 ; """
#         expect = """Program([\n\tVarDecl(_huy_29_n, ArrayType([4101], StringType), BinExpr(!=, StringLit(quan \\b), StringLit(huy \\f)))\n\tVarDecl(__29_, ArrayType([4101], StringType), BinExpr(>, IntegerLit(31112123), IntegerLit(4123)))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 314))
#     def test_15(self):
#         """test 15"""
#         input = """_huy_Depay, __Huy_29 : boolean  = {true,false,true,false}, 2_12_12 <= 4_111_29 ;
#                     a,b:  float = 1_02.2e-1 >= 1_01.3e-3, a+10/2*3.e1-x_29 ;"""
#         expect = """Program([\n\tVarDecl(_huy_Depay, BooleanType, ArrayLit([BooleanLit(True), BooleanLit(False), BooleanLit(True), BooleanLit(False)]))\n\tVarDecl(__Huy_29, BooleanType, BinExpr(<=, IntegerLit(21212), IntegerLit(411129)))\n\tVarDecl(a, FloatType, BinExpr(>=, FloatLit(10.22), FloatLit(0.1013)))\n\tVarDecl(b, FloatType, BinExpr(-, BinExpr(+, Id(a), BinExpr(*, BinExpr(/, IntegerLit(10), IntegerLit(2)), FloatLit(30.0))), Id(x_29)))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 315))
#     def test_16(self):
#         """test 16"""
#         input = """_huy_12_1, _messi : float  = 2_12 +- 5_1_1_02, !29%5 ;
#                     a,b:  string = "huy \\"dang hoc\\" bi quan pha ", "quan bip bom"=="huy that tha" ;"""
#         expect = """Program([\n\tVarDecl(_huy_12_1, FloatType, BinExpr(+, IntegerLit(212), UnExpr(-, IntegerLit(51102))))\n\tVarDecl(_messi, FloatType, BinExpr(%, UnExpr(!, IntegerLit(29)), IntegerLit(5)))\n\tVarDecl(a, StringType, StringLit(huy \\"dang hoc\\" bi quan pha ))\n\tVarDecl(b, StringType, BinExpr(==, StringLit(quan bip bom), StringLit(huy that tha)))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 316))
#     def test_17(self):
#         """test 17"""
#         input = """_huy29_10 : array[1_23,2_21] of float = {"huy dang hoc", "huy co gang \\"hoc that tot \\t\\""}  ;
#                     a,b:  integer = 12_102 -- 29_1_9_0, quan[23_12, 32_1_2_06] ;"""
#         expect = """Program([\n\tVarDecl(_huy29_10, ArrayType([123, 221], FloatType), ArrayLit([StringLit(huy dang hoc), StringLit(huy co gang \\"hoc that tot \\t\\")]))\n\tVarDecl(a, IntegerType, BinExpr(-, IntegerLit(12102), UnExpr(-, IntegerLit(29190))))\n\tVarDecl(b, IntegerType, ArrayCell(quan, [IntegerLit(2312), IntegerLit(321206)]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 317))
#     def test_18(self):
#         """test 18"""
#         input = """__29_10 : integer = -3+29*9/10+4 ;
#                     d, c: float = !12.e3, quan || huy && thanh   ;
#                     e_1 : array[234_1,2_305,21_9,32_2] of float; """
#         expect = """Program([\n\tVarDecl(__29_10, IntegerType, BinExpr(+, BinExpr(+, UnExpr(-, IntegerLit(3)), BinExpr(/, BinExpr(*, IntegerLit(29), IntegerLit(9)), IntegerLit(10))), IntegerLit(4)))\n\tVarDecl(d, FloatType, UnExpr(!, FloatLit(12000.0)))\n\tVarDecl(c, FloatType, BinExpr(&&, BinExpr(||, Id(quan), Id(huy)), Id(thanh)))\n\tVarDecl(e_1, ArrayType([2341, 2305, 219, 322], FloatType))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 318))
#     def test_19(self):
#         """test 19"""
#         input = """ ___2711_quan: string = "huy dang hoc \\f\\t" :: "huy chay deadline" == "quan choi game" ;
#                      """
#         expect = """Program([\n\tVarDecl(___2711_quan, StringType, BinExpr(::, StringLit(huy dang hoc \\f\\t), BinExpr(==, StringLit(huy chay deadline), StringLit(quan choi game))))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 319))
#     def test_20(self):
#         """test 20"""
#         input = """ _2910_huy: float = __huy(2_12*me(1.23+2_1.e1/12_02*12--12)) ;
#                     _09_10,h,u,y: integer = true,false,hello,2.3e+1;
#                     a_2910_02: string;
#                      """
#         expect = """Program([\n\tVarDecl(_2910_huy, FloatType, FuncCall(__huy, [BinExpr(*, IntegerLit(212), FuncCall(me, [BinExpr(-, BinExpr(+, FloatLit(1.23), BinExpr(*, BinExpr(/, FloatLit(210.0), IntegerLit(1202)), IntegerLit(12))), UnExpr(-, IntegerLit(12)))]))]))\n\tVarDecl(_09_10, IntegerType, BooleanLit(True))\n\tVarDecl(h, IntegerType, BooleanLit(False))\n\tVarDecl(u, IntegerType, Id(hello))\n\tVarDecl(y, IntegerType, FloatLit(23.0))\n\tVarDecl(a_2910_02, StringType)\n])"""
#         self.assertTrue(TestAST.test(input, expect, 320))
#     def test_21(self):
#         """test 21"""
#         input = """ _29_huy: string = {"huy", "huy dang lam testcase \\t\\f"};
#                     _baba_2404: integer = !-12*23+3*4 ;
#                      """
#         expect = """Program([\n\tVarDecl(_29_huy, StringType, ArrayLit([StringLit(huy), StringLit(huy dang lam testcase \\t\\f)]))\n\tVarDecl(_baba_2404, IntegerType, BinExpr(+, BinExpr(*, UnExpr(!, UnExpr(-, IntegerLit(12))), IntegerLit(23)), BinExpr(*, IntegerLit(3), IntegerLit(4))))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 321))
#     def test_22(self):
#         """test 22"""
#         input = """ _29_mami: float = {"huy", "huy dang di hoc \\b\\n"};
#                     _baba_2404: integer = !-12*23+3*4 ;
#                      """
#         expect = """Program([\n\tVarDecl(_29_mami, FloatType, ArrayLit([StringLit(huy), StringLit(huy dang di hoc \\b\\n)]))\n\tVarDecl(_baba_2404, IntegerType, BinExpr(+, BinExpr(*, UnExpr(!, UnExpr(-, IntegerLit(12))), IntegerLit(23)), BinExpr(*, IntegerLit(3), IntegerLit(4))))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 322))
#     def test_23(self):
#         """test 23"""
#         input = """ _mami0606: integer = 12321.2e1+1_123--3_21*1.2e+1;
#                     _baba_2404: string = "huy dang lam test case \\f\\"dung lam phien huy\\t\\"";
#                      """
#         expect = """Program([\n\tVarDecl(_mami0606, IntegerType, BinExpr(-, BinExpr(+, FloatLit(123212.0), IntegerLit(1123)), BinExpr(*, UnExpr(-, IntegerLit(321)), FloatLit(12.0))))\n\tVarDecl(_baba_2404, StringType, StringLit(huy dang lam test case \\f\\"dung lam phien huy\\t\\"))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 323))
#     def test_24(self):
#         """test 24"""
#         input = """ __039, ache_24: array [1_2, 2_13, 4_12] of string = !-1_234e+1-24_123/1_11, {huy, true, 2_123.23, 1_032, "quan coc huy \\b\\"huy khoc \\f\\""};
#                      """
#         expect = """Program([\n\tVarDecl(__039, ArrayType([12, 213, 412], StringType), BinExpr(-, UnExpr(!, UnExpr(-, FloatLit(12340.0))), BinExpr(/, IntegerLit(24123), IntegerLit(111))))\n\tVarDecl(ache_24, ArrayType([12, 213, 412], StringType), ArrayLit([Id(huy), BooleanLit(True), FloatLit(2123.23), IntegerLit(1032), StringLit(quan coc huy \\b\\"huy khoc \\f\\")]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 324))
#     def test_25(self):
#         """test 25"""
#         input = """ ____, huy_29_, mf_1: auto = "quan" :: "huy dang hoc \\f" < "thanh cay phim" || hello_friend, !-1234.23e-1, messi(2_12/x) ;
#                      """
#         expect = """Program([\n\tVarDecl(____, AutoType, BinExpr(::, StringLit(quan), BinExpr(<, StringLit(huy dang hoc \\f), BinExpr(||, StringLit(thanh cay phim), Id(hello_friend)))))\n\tVarDecl(huy_29_, AutoType, UnExpr(!, UnExpr(-, FloatLit(123.423))))\n\tVarDecl(mf_1, AutoType, FuncCall(messi, [BinExpr(/, IntegerLit(212), Id(x))]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 325))
#     def test_26(self):
#         """test 26"""
#         input = """ quan_27, cuong_1808: integer = 123_123_1_0_1_12, 2910.2e-1 ;
#                     a,c,d: string; """
#         expect = """Program([\n\tVarDecl(quan_27, IntegerType, IntegerLit(12312310112))\n\tVarDecl(cuong_1808, IntegerType, FloatLit(291.02))\n\tVarDecl(a, StringType)\n\tVarDecl(c, StringType)\n\tVarDecl(d, StringType)\n])"""
#         self.assertTrue(TestAST.test(input, expect, 326))
#     def test_27(self):
#         """test 27"""
#         input = """huy_29: function integer (a: integer, b: string, e: boolean){
#         } """
#         expect = """Program([\n\tFuncDecl(huy_29, IntegerType, [Param(a, IntegerType), Param(b, StringType), Param(e, BooleanType)], None, BlockStmt([]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 327))
#     def test_28(self):
#         """test 28"""
#         input = """huy_29: function integer (a: integer, b: string, e: boolean){
#             goo();
#         } """
#         expect = """Program([\n\tFuncDecl(huy_29, IntegerType, [Param(a, IntegerType), Param(b, StringType), Param(e, BooleanType)], None, BlockStmt([CallStmt(goo, )]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 328))
#     def test_29(self):
#         """test 29"""
#         input = """inc: function void (out a: integer, delta: integer){
#             n = n + delta;
#         } """
#         expect = """Program([\n\tFuncDecl(inc, VoidType, [OutParam(a, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 327))
#     def test_30(self):
#         """test 30"""
#         input = """__29: function auto (inherit out huy_29: string, out _h__: float, __: integer) inherit quan_thay{
#             if (i == 1)
#                 return i;
#         } """
#         expect = """Program([\n\tFuncDecl(__29, AutoType, [InheritOutParam(huy_29, StringType), OutParam(_h__, FloatType), Param(__, IntegerType)], quan_thay, BlockStmt([IfStmt(BinExpr(==, Id(i), IntegerLit(1)), ReturnStmt(Id(i)))]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 330))
#     def test_31(self):
#         """test 31"""
#         input = """x : integer=65;
#         fact : function integer(n : integer) {
#         if ( n == 0 ) return 1 ;
#         else return n * fact(n - 1 ) ;
#         }
#         inc : function void (out n : integer , delta : integer) {
#         n = n + delta ;
#         }
#         main : function void () {
#         delta : integer = fact(3) ;
#         inc(x ,delta ) ;
#         printInteger(x) ;
#         }
#         """
#         expect = """Program([\n\tVarDecl(x, IntegerType, IntegerLit(65))\n\tFuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))\n\tFuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))\n\tFuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)])), CallStmt(inc, Id(x), Id(delta)), CallStmt(printInteger, Id(x))]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 331))
#     def test_32(self):
#         """test 32"""
#         input = """main: function void () {
#         x: integer = 3;
#         }"""
#         expect = """Program([\n\tFuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(3))]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 332))
#     def test_33(self):
#         """test 33"""
#         input = """__1902: function array[1_22_123_1] of integer (inherit yeu_29: array[52_12, 1_2] of string, out _: integer, d_12: boolean) {
#         for (i = 1, i < 10, i + 1) {
#             writeInt(i);
#             }
#         }"""
#         expect = """Program([\n\tFuncDecl(__1902, ArrayType([1221231], IntegerType), [InheritParam(yeu_29, ArrayType([5212, 12], StringType)), OutParam(_, IntegerType), Param(d_12, BooleanType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writeInt, Id(i))]))]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 333))
#     def test_34(self):
#         """test 34"""
#         input = """hello: function string (inherit out a: integer, out b29: string) inherit function_name{
#             de_29, huy_9: integer = true, 12.31e+1;
#             do {
#                 r, s: integer;
#                 r = 2.0;
#                 a, b: array [5] of integer;
#                 s = r * r * myPI;
#                 a[0] = s;
#                 }
#             while ("quan" != "huy" );
#             }"""
#         expect = """Program([\n\tFuncDecl(hello, StringType, [InheritOutParam(a, IntegerType), OutParam(b29, StringType)], function_name, BlockStmt([VarDecl(de_29, IntegerType, BooleanLit(True)), VarDecl(huy_9, IntegerType, FloatLit(123.1)), DoWhileStmt(BinExpr(!=, StringLit(quan), StringLit(huy)), BlockStmt([VarDecl(r, IntegerType), VarDecl(s, IntegerType), AssignStmt(Id(r), FloatLit(2.0)), VarDecl(a, ArrayType([5], IntegerType)), VarDecl(b, ArrayType([5], IntegerType)), AssignStmt(Id(s), BinExpr(*, BinExpr(*, Id(r), Id(r)), Id(myPI))), AssignStmt(ArrayCell(a, [IntegerLit(0)]), Id(s))]))]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 334))
#     def test_35(self):
#         """test 35"""
#         input = """
#         /* Huy chua co bo */
#         x, y : boolean = !true, "false";
#         main: function void (out n: integer,inherit i: string) inherit foo {
#             /* Multiple expr in condition and scalar var for init */
#             for (a[a[0, 1_2]] = 0, (a < 1_0.20) || !false, a*-2) x = x*(2+y);
#         }
#         """
#         expect = """Program([\n\tVarDecl(x, BooleanType, UnExpr(!, BooleanLit(True)))\n\tVarDecl(y, BooleanType, StringLit(false))\n\tFuncDecl(main, VoidType, [OutParam(n, IntegerType), InheritParam(i, StringType)], foo, BlockStmt([ForStmt(AssignStmt(ArrayCell(a, [ArrayCell(a, [IntegerLit(0), IntegerLit(12)])]), IntegerLit(0)), BinExpr(||, BinExpr(<, Id(a), FloatLit(10.2)), UnExpr(!, BooleanLit(False))), BinExpr(*, Id(a), UnExpr(-, IntegerLit(2))), AssignStmt(Id(x), BinExpr(*, Id(x), BinExpr(+, IntegerLit(2), Id(y)))))]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 335))
#     def test_36(self):
#         """test 36"""
#         input = """
#             x, y, z: integer = "hello\\"Quynh Lam\\"\\t ne", 1_23_45.21000, foo(bar(), a);
#             t: array [1_0, 2_0] of string = {"\\"Lam khong yeu Huy\\""};
#             func: function void (inherit out x: array [0, 1] of boolean, out i: string) {
#                 {
#                     // Empty block
#                 }
#                 {
#                     /* Empty block */
#                     {
#                         print("Hello");
#                     }
#                 }
#             }
#         """
#         expect = """Program([\n\tVarDecl(x, IntegerType, StringLit(hello\\"Quynh Lam\\"\\t ne))\n\tVarDecl(y, IntegerType, FloatLit(12345.21))\n\tVarDecl(z, IntegerType, FuncCall(foo, [FuncCall(bar, []), Id(a)]))\n\tVarDecl(t, ArrayType([10, 20], StringType), ArrayLit([StringLit(\\"Lam khong yeu Huy\\")]))\n\tFuncDecl(func, VoidType, [InheritOutParam(x, ArrayType([0, 1], BooleanType)), OutParam(i, StringType)], None, BlockStmt([BlockStmt([]), BlockStmt([BlockStmt([CallStmt(print, StringLit(Hello))])])]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 336))
#     def test_37(self):
#         """test 37"""
#         input = """huy_29, quan_27: array[12_1,21_3] of boolean= {"quan luot tiktok \\"ko trl tin nhan nhi\\"", "nhi buon nhi khoc"}, 123_12.e+3;
#                 friend_29: function void (inherit b: integer, out a: string) inherit quandeptrai{
#                 while (a < a+1)
#                  a[213, 3_12] = 29;
#                  break;
#                 } """
#         expect = """Program([\n\tVarDecl(huy_29, ArrayType([121, 213], BooleanType), ArrayLit([StringLit(quan luot tiktok \\"ko trl tin nhan nhi\\"), StringLit(nhi buon nhi khoc)]))\n\tVarDecl(quan_27, ArrayType([121, 213], BooleanType), FloatLit(12312000.0))\n\tFuncDecl(friend_29, VoidType, [InheritParam(b, IntegerType), OutParam(a, StringType)], quandeptrai, BlockStmt([WhileStmt(BinExpr(<, Id(a), BinExpr(+, Id(a), IntegerLit(1))), AssignStmt(ArrayCell(a, [IntegerLit(213), IntegerLit(312)]), IntegerLit(29))), BreakStmt()]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 337))
#     def test_38(self):
#         """test 38"""
#         input = """__, _2_9_10: integer= {"quan con choi insta ko", hello, 12_2_9_0_1_123, 1_2.e-1}, foo(2/x);
#                 main: function string (inherit a_29: string, out quan__27: array[2_1] of boolean) inherit lam_testcae {
#                     if (a != 23)
#                         return foo(4+y);
                    
#                     else{
#                         messi(2+x/y*3);
#                         continue;
#                     }
#                 }  """
#         expect = """Program([\n\tVarDecl(__, IntegerType, ArrayLit([StringLit(quan con choi insta ko), Id(hello), IntegerLit(122901123), FloatLit(1.2)]))\n\tVarDecl(_2_9_10, IntegerType, FuncCall(foo, [BinExpr(/, IntegerLit(2), Id(x))]))\n\tFuncDecl(main, StringType, [InheritParam(a_29, StringType), OutParam(quan__27, ArrayType([21], BooleanType))], lam_testcae, BlockStmt([IfStmt(BinExpr(!=, Id(a), IntegerLit(23)), ReturnStmt(FuncCall(foo, [BinExpr(+, IntegerLit(4), Id(y))])), BlockStmt([CallStmt(messi, BinExpr(+, IntegerLit(2), BinExpr(*, BinExpr(/, Id(x), Id(y)), IntegerLit(3)))), ContinueStmt()]))]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 338))
#     def test_39(self):
#         """test 39"""
#         input = """
#                 main: function string (inherit a_29: string, out quan__27: array[2_1] of boolean) inherit lam_testcae {
#                     hello_quan: integer = {"quan luot tiktok"};
#                     for (i = 1, i < 2,  x+y*z/t+--2_3){
#                         for (a[21,12_2_0] = 2, a < 12.e+1, a+1)
#                         {
#                             return;
#                         }
#                         i = i+1;
#                     }
#                 }  """
#         expect = """Program([\n\tFuncDecl(main, StringType, [InheritParam(a_29, StringType), OutParam(quan__27, ArrayType([21], BooleanType))], lam_testcae, BlockStmt([VarDecl(hello_quan, IntegerType, ArrayLit([StringLit(quan luot tiktok)])), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(2)), BinExpr(+, BinExpr(+, Id(x), BinExpr(/, BinExpr(*, Id(y), Id(z)), Id(t))), UnExpr(-, UnExpr(-, IntegerLit(23)))), BlockStmt([ForStmt(AssignStmt(ArrayCell(a, [IntegerLit(21), IntegerLit(1220)]), IntegerLit(2)), BinExpr(<, Id(a), FloatLit(120.0)), BinExpr(+, Id(a), IntegerLit(1)), BlockStmt([ReturnStmt()])), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 339))
#     def test_40(self):
#         """test 40"""
#         input = """__huy_10: integer = !!- aaa;
#         i_29: function boolean () {
#         while (i < 1)
#             i = i+1;
#         }  """
#         expect = """Program([\n\tVarDecl(__huy_10, IntegerType, UnExpr(!, UnExpr(!, UnExpr(-, Id(aaa)))))\n\tFuncDecl(i_29, BooleanType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(i), IntegerLit(1)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))))]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 340))
#     def test_41(self):
#         """test 41"""
#         input = """__huy_10: integer = .e23 ;
#                 _29quan: function array[29,19_1] of string () inherit ___{
#                     if (a[][] <= 2)
#                         return fact(n-1);
#                 }"""
#         expect = """Program([\n\tVarDecl(__huy_10, IntegerType, FloatLit(0.0))\n\tFuncDecl(_29quan, ArrayType([29, 191], StringType), [], ___, BlockStmt([IfStmt(BinExpr(<=, UnExpr(], UnExpr([, UnExpr(], UnExpr([, Id(a))))), IntegerLit(2)), ReturnStmt(FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))])))]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 341))
#     def test_42(self):
#         """test 42"""
#         input = """
#                 _29quan: function array[29,19_1] of string () inherit ___{
#                     huy_29: float = .1e23 ;
#                     while (!- __huy < 21.3)
#                     {
#                         while (_quan_29 >= !"huy \\"huy\\t\\"")
#                         {
#                             i = huy :: "quan" <= .e-23;
#                         }
#                         i = i + 1;
#                     }
#                 }"""
#         expect = """Program([\n\tFuncDecl(_29quan, ArrayType([29, 191], StringType), [], ___, BlockStmt([VarDecl(huy_29, FloatType, FloatLit(1e+22)), WhileStmt(BinExpr(<, UnExpr(!, UnExpr(-, Id(__huy))), FloatLit(21.3)), BlockStmt([WhileStmt(BinExpr(>=, Id(_quan_29), UnExpr(!, StringLit(huy \\"huy\\t\\"))), BlockStmt([AssignStmt(Id(i), BinExpr(::, Id(huy), BinExpr(<=, StringLit(quan), FloatLit(0.0))))])), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 342))
#     def test_43(self):
#         """test 43"""
#         input = """
#                 _huy: array[21_1_2, 123_29] of boolean = {"huy dang lam testcase \\"quan di choi\\""};
#                 main: function void()
#                 {
#                 if (a < a +1){
#                     a,b: integer = a[a[1_2,2_1]], .e-23;
#                 }
#                 } 
#                 """
#         expect = """Program([\n\tVarDecl(_huy, ArrayType([2112, 12329], BooleanType), ArrayLit([StringLit(huy dang lam testcase \\"quan di choi\\")]))\n\tFuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(<, Id(a), BinExpr(+, Id(a), IntegerLit(1))), BlockStmt([VarDecl(a, IntegerType, ArrayCell(a, [ArrayCell(a, [IntegerLit(12), IntegerLit(21)])])), VarDecl(b, IntegerType, FloatLit(0.0))]))]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 343))
#     def test_44(self):
#         """test 44"""
#         input = """
#                 a,b,c: integer= 12.32e+2, "huy dang lam bai \\"quan di choi \\b\\t\\"", ba_24; //test case
#                 mami_06: function auto (inherit d: integer, out a: string, inherit out d: float) inherit bye_ars{
#                  for (i = 2/x+3*2*d, i != -3, i || d || c){
#                         if (i != huy_29_1)
#                         {
#                             return foo();
#                         }
#                         else
#                         {
#                         a = a+1;
#                         }
#                         hellomessi(i+1);
#                     }   
#                 }"""
#         expect = """Program([\n\tVarDecl(a, IntegerType, FloatLit(1232.0))\n\tVarDecl(b, IntegerType, StringLit(huy dang lam bai \\"quan di choi \\b\\t\\"))\n\tVarDecl(c, IntegerType, Id(ba_24))\n\tFuncDecl(mami_06, AutoType, [InheritParam(d, IntegerType), OutParam(a, StringType), InheritOutParam(d, FloatType)], bye_ars, BlockStmt([ForStmt(AssignStmt(Id(i), BinExpr(+, BinExpr(/, IntegerLit(2), Id(x)), BinExpr(*, BinExpr(*, IntegerLit(3), IntegerLit(2)), Id(d)))), BinExpr(!=, Id(i), UnExpr(-, IntegerLit(3))), BinExpr(||, BinExpr(||, Id(i), Id(d)), Id(c)), BlockStmt([IfStmt(BinExpr(!=, Id(i), Id(huy_29_1)), BlockStmt([ReturnStmt(FuncCall(foo, []))]), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))])), CallStmt(hellomessi, BinExpr(+, Id(i), IntegerLit(1)))]))]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 344))
#     def test_45(self):
#         """test 45"""
#         input = """
#         huy2910: function void(){
#             do{
#                 a[0,1_2_3] = x+1--2;
#                 _quan: integer = .e-2353;
#                 while (_hello :: "huyhamhoc" || "quan ham choi")
#                 {
#                     t = "dung 4/5 da finish";
#                 }
#             }
#             while (i < i+1);
#         }
#         """
#         expect = """Program([\n\tFuncDecl(huy2910, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, Id(i), BinExpr(+, Id(i), IntegerLit(1))), BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(0), IntegerLit(123)]), BinExpr(-, BinExpr(+, Id(x), IntegerLit(1)), UnExpr(-, IntegerLit(2)))), VarDecl(_quan, IntegerType, FloatLit(0.0)), WhileStmt(BinExpr(::, Id(_hello), BinExpr(||, StringLit(huyhamhoc), StringLit(quan ham choi))), BlockStmt([AssignStmt(Id(t), StringLit(dung 4/5 da finish))]))]))]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 345))
#     def test_46(self):
#         """test 46"""
#         input = """
#         i_nc: function auto() inherit he_llo{
#             a: integer = 123----234+3*2/3;
#             return;
#             break;
#             continue;
#         }
#         """
#         expect = """Program([\n\tFuncDecl(i_nc, AutoType, [], he_llo, BlockStmt([VarDecl(a, IntegerType, BinExpr(+, BinExpr(-, IntegerLit(123), UnExpr(-, UnExpr(-, UnExpr(-, IntegerLit(234))))), BinExpr(/, BinExpr(*, IntegerLit(3), IntegerLit(2)), IntegerLit(3)))), ReturnStmt(), BreakStmt(), ContinueStmt()]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 346))
#     def test_47(self):
#         """test 47"""
#         input = """
#         i_nc: function auto(a: array[12_1,29_1] of string) {
#             if (a == !---384*4+d_a) break;
#             else continue;
#         }
#         """
#         expect = """Program([\n\tFuncDecl(i_nc, AutoType, [Param(a, ArrayType([121, 291], StringType))], None, BlockStmt([IfStmt(BinExpr(==, Id(a), BinExpr(+, BinExpr(*, UnExpr(!, UnExpr(-, UnExpr(-, UnExpr(-, IntegerLit(384))))), IntegerLit(4)), Id(d_a))), BreakStmt(), ContinueStmt())]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 347))
#     def test_48(self):
#         """test 48"""
#         input = """
#         ache_0309: function integer(inherit out _01_: integer, out a_01: string) {
#             if (a == !-23) break;
#             else {
#                 while ( i <= i + .e-789)
#                 {
#                     smt = "quan qua au \\"bi sai 1 test case \\t\\"";
#                 }
#             }
#         }
#         """
#         expect = """Program([\n\tFuncDecl(ache_0309, IntegerType, [InheritOutParam(_01_, IntegerType), OutParam(a_01, StringType)], None, BlockStmt([IfStmt(BinExpr(==, Id(a), UnExpr(!, UnExpr(-, IntegerLit(23)))), BreakStmt(), BlockStmt([WhileStmt(BinExpr(<=, Id(i), BinExpr(+, Id(i), FloatLit(0.0))), BlockStmt([AssignStmt(Id(smt), StringLit(quan qua au \\"bi sai 1 test case \\t\\"))]))]))]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 348))
#     def test_49(self):
#         """test 49"""
#         input = """
#         baba_24: array[29_1, 12_23, 1_90, 3_78] of boolean = hello[123, 29.1e+1]; /* dang lam bieng */
#         mami_06: float = {"quan dang di choi \\"xong bi gian khoc \\" khoc huhu \\t"}; //testcase
#         ache_0309: function integer() inherit huy_2910 {
#             for (i = a+1*2/3, i < i+2, "huy_29\\b" && "quan_27\\t")
#             {
#                 if (!"quan luoi hoc" :: "quan can than")
#                  return "quan diem cao";
#                 else saunay[12_3,4_89] = "quan khoc huhu \\"doi huy bao nc\\"";
#             }
#         }
#         """
#         expect = """Program([\n\tVarDecl(baba_24, ArrayType([291, 1223, 190, 378], BooleanType), ArrayCell(hello, [IntegerLit(123), FloatLit(291.0)]))\n\tVarDecl(mami_06, FloatType, ArrayLit([StringLit(quan dang di choi \\"xong bi gian khoc \\" khoc huhu \\t)]))\n\tFuncDecl(ache_0309, IntegerType, [], huy_2910, BlockStmt([ForStmt(AssignStmt(Id(i), BinExpr(+, Id(a), BinExpr(/, BinExpr(*, IntegerLit(1), IntegerLit(2)), IntegerLit(3)))), BinExpr(<, Id(i), BinExpr(+, Id(i), IntegerLit(2))), BinExpr(&&, StringLit(huy_29\\b), StringLit(quan_27\\t)), BlockStmt([IfStmt(BinExpr(::, UnExpr(!, StringLit(quan luoi hoc)), StringLit(quan can than)), ReturnStmt(StringLit(quan diem cao)), AssignStmt(ArrayCell(saunay, [IntegerLit(123), IntegerLit(489)]), StringLit(quan khoc huhu \\"doi huy bao nc\\")))]))]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 349))
#     def test_50(self):
#         """test 50"""
#         input = """
#         sadboiz_huy: boolean = true;
#         trapboy_thanh: float = .e23 + 12/4*2_9-10;
#         quanbipbom: function void() inherit hello{
#             if ("cuong gam giuong" :: "bik qua nhiu" != "dung su that")
#                 return "cuong noi xao \\"qua choi\\" lun do \\f";
#             else{
#                 do{
#                     huychamhoc: integer = 29_10;
#                     thanhdsa: float = .1e-1;
#                 }
#                 while (quan != "im mom di");
#             }
#         }
#         """
#         expect = """Program([\n\tVarDecl(sadboiz_huy, BooleanType, BooleanLit(True))\n\tVarDecl(trapboy_thanh, FloatType, BinExpr(-, BinExpr(+, FloatLit(0.0), BinExpr(*, BinExpr(/, IntegerLit(12), IntegerLit(4)), IntegerLit(29))), IntegerLit(10)))\n\tFuncDecl(quanbipbom, VoidType, [], hello, BlockStmt([IfStmt(BinExpr(::, StringLit(cuong gam giuong), BinExpr(!=, StringLit(bik qua nhiu), StringLit(dung su that))), ReturnStmt(StringLit(cuong noi xao \\"qua choi\\" lun do \\f)), BlockStmt([DoWhileStmt(BinExpr(!=, Id(quan), StringLit(im mom di)), BlockStmt([VarDecl(huychamhoc, IntegerType, IntegerLit(2910)), VarDecl(thanhdsa, FloatType, FloatLit(0.01))]))]))]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 350))
#     def test_51(self):
#         """test 51"""
#         input = """
#         main: function auto(inherit __: string, out huy_29: integer){
#             if ((huy != "quan ham hoc") && (a != b)) {
#                 hello = "quan bip bom";
#                 a_29: array[29_10] of integer = {123_32, "quan \\"huy di hoc \\b\\t\\""};
#             }
#             else
#             {
#                 for ( a[a[123_1, 1243]] = 123_343, i < 29_12, i +1)
#                 {
#                     return fact(n-1) * (n+2);
#                 }
#             }
#         }
#         """
#         expect = """Program([\n\tFuncDecl(main, AutoType, [InheritParam(__, StringType), OutParam(huy_29, IntegerType)], None, BlockStmt([IfStmt(BinExpr(&&, BinExpr(!=, Id(huy), StringLit(quan ham hoc)), BinExpr(!=, Id(a), Id(b))), BlockStmt([AssignStmt(Id(hello), StringLit(quan bip bom)), VarDecl(a_29, ArrayType([2910], IntegerType), ArrayLit([IntegerLit(12332), StringLit(quan \\"huy di hoc \\b\\t\\")]))]), BlockStmt([ForStmt(AssignStmt(ArrayCell(a, [ArrayCell(a, [IntegerLit(1231), IntegerLit(1243)])]), IntegerLit(123343)), BinExpr(<, Id(i), IntegerLit(2912)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ReturnStmt(BinExpr(*, FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]), BinExpr(+, Id(n), IntegerLit(2))))]))]))]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 351))
#     def test_52(self):
#         """test 52"""
#         input = """
#         __huy_13, quan_2711: array[43_32, 1_03, 4_0] of boolean = {"quan ham choi \\n\\t\\"huy di hoc\\""}, .e-123;
#         m_quan_2910: function array[32_12, 432] of string(inherit d: integer) inherit _ {
#             while ((huy_29 != 29_04) && (quan_27 <= huy_2910) || (haha > huhu))
#             {
#                 do {
#                     solution: boolean = true;
#                     t_c_18: float = .e-2321;
#                     do{
#                         return foodboy(n_291+2/3);
#                     }
#                     while (huy_29 < 32*21);
#                 } while (quan_331 >= 21*.e23/12_12);
#                 a_27: integer = 123_24;
#             } 
#             katinat: array [12_1,3_45] of boolean = "huy_29 \\" huy di hoc\\"";
#         }
#         """
#         expect = """Program([\n\tVarDecl(__huy_13, ArrayType([4332, 103, 40], BooleanType), ArrayLit([StringLit(quan ham choi \\n\\t\\"huy di hoc\\")]))\n\tVarDecl(quan_2711, ArrayType([4332, 103, 40], BooleanType), FloatLit(0.0))\n\tFuncDecl(m_quan_2910, ArrayType([3212, 432], StringType), [InheritParam(d, IntegerType)], _, BlockStmt([WhileStmt(BinExpr(||, BinExpr(&&, BinExpr(!=, Id(huy_29), IntegerLit(2904)), BinExpr(<=, Id(quan_27), Id(huy_2910))), BinExpr(>, Id(haha), Id(huhu))), BlockStmt([DoWhileStmt(BinExpr(>=, Id(quan_331), BinExpr(/, BinExpr(*, IntegerLit(21), FloatLit(0.0)), IntegerLit(1212))), BlockStmt([VarDecl(solution, BooleanType, BooleanLit(True)), VarDecl(t_c_18, FloatType, FloatLit(0.0)), DoWhileStmt(BinExpr(<, Id(huy_29), BinExpr(*, IntegerLit(32), IntegerLit(21))), BlockStmt([ReturnStmt(FuncCall(foodboy, [BinExpr(+, Id(n_291), BinExpr(/, IntegerLit(2), IntegerLit(3)))]))]))])), VarDecl(a_27, IntegerType, IntegerLit(12324))])), VarDecl(katinat, ArrayType([121, 345], BooleanType), StringLit(huy_29 \\" huy di hoc\\"))]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 352))
#     def test_53(self):
#         """test 53"""
#         input = """
#         huy: integer = 123_21.e+23;
#         i_29_quan: float = .e-294;
#         main: function void(){
#             if (huy != 2334_72987 && (quan == "quan cham chi \\"quan ham hoc\\"")){
#                 for (huy_29 = 38*28/323+12.23e2, huy < "huy 10 diem \\"huy di choi\\"", !-huy+quan/29){
#                     continue;
#                 }
#                 break;
#             }
#             messi(2/3+1*2*2+quan);
#         } 
#         """
#         expect = """Program([\n\tVarDecl(huy, IntegerType, FloatLit(1.2321e+27))\n\tVarDecl(i_29_quan, FloatType, FloatLit(0.0))\n\tFuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(!=, Id(huy), BinExpr(&&, IntegerLit(233472987), BinExpr(==, Id(quan), StringLit(quan cham chi \\"quan ham hoc\\")))), BlockStmt([ForStmt(AssignStmt(Id(huy_29), BinExpr(+, BinExpr(/, BinExpr(*, IntegerLit(38), IntegerLit(28)), IntegerLit(323)), FloatLit(1223.0))), BinExpr(<, Id(huy), StringLit(huy 10 diem \\"huy di choi\\")), BinExpr(+, UnExpr(!, UnExpr(-, Id(huy))), BinExpr(/, Id(quan), IntegerLit(29))), BlockStmt([ContinueStmt()])), BreakStmt()])), CallStmt(messi, BinExpr(+, BinExpr(+, BinExpr(/, IntegerLit(2), IntegerLit(3)), BinExpr(*, BinExpr(*, IntegerLit(1), IntegerLit(2)), IntegerLit(2))), Id(quan)))]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 353))
#     def test_54(self):
#         """test 54"""
#         input = """
#         a_29, huy_123: array[39_10] of integer = {.E2, "quan \\"huy di hoc \\b\\t\\"", true}, {12.29E-10, "huy", false};
#         hello: function void(){
#             return stmt;
#             continue;
#             break;
#         }
#         """
#         expect = """Program([\n\tVarDecl(a_29, ArrayType([3910], IntegerType), ArrayLit([FloatLit(0.0), StringLit(quan \\"huy di hoc \\b\\t\\"), BooleanLit(True)]))\n\tVarDecl(huy_123, ArrayType([3910], IntegerType), ArrayLit([FloatLit(1.229e-09), StringLit(huy), BooleanLit(False)]))\n\tFuncDecl(hello, VoidType, [], None, BlockStmt([ReturnStmt(Id(stmt)), ContinueStmt(), BreakStmt()]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 354))
#     def test_55(self):
#         """test 55"""
#         input = """
#         huy_12: integer = 12_21_2_1.E-10;
#         hi: function integer (inherit a_29: integer, out d: string, inherit out h_09: float, m: boolean) inherit bye{
#             saygoodbye();
#             do{
#                 if (!!----a_29 || b * 7_89){
#                     if (hello< 12_29){
#                         huy(29/123*2+1/231);
#                     }
#                     else continue;
#                 }
#                 else{
#                     sieunhan(32+321/3_1e1 || true % "quantretrau");
#                 }
#             }
#             while (a != false);
#         }
#         """
#         expect = """Program([\n\tVarDecl(huy_12, IntegerType, FloatLit(1.22121e-05))\n\tFuncDecl(hi, IntegerType, [InheritParam(a_29, IntegerType), OutParam(d, StringType), InheritOutParam(h_09, FloatType), Param(m, BooleanType)], bye, BlockStmt([CallStmt(saygoodbye, ), DoWhileStmt(BinExpr(!=, Id(a), BooleanLit(False)), BlockStmt([IfStmt(BinExpr(||, UnExpr(!, UnExpr(!, UnExpr(-, UnExpr(-, UnExpr(-, UnExpr(-, Id(a_29))))))), BinExpr(*, Id(b), IntegerLit(789))), BlockStmt([IfStmt(BinExpr(<, Id(hello), IntegerLit(1229)), BlockStmt([CallStmt(huy, BinExpr(+, BinExpr(*, BinExpr(/, IntegerLit(29), IntegerLit(123)), IntegerLit(2)), BinExpr(/, IntegerLit(1), IntegerLit(231))))]), ContinueStmt())]), BlockStmt([CallStmt(sieunhan, BinExpr(||, BinExpr(+, IntegerLit(32), BinExpr(/, IntegerLit(321), FloatLit(310.0))), BinExpr(%, BooleanLit(True), StringLit(quantretrau))))]))]))]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 355))
#     def test_56(self):
#         """test 56"""
#         input = """
#         huy_12: float = .E-10;
#         __: boolean = true;
#         _291: function void(){
#             for (a[a[a[29_10, 9_89]]] = true, hey < hey + ---2, hi --2){
#                 for (a[304] = foo(2*3), i < 1, i --2){
#                     saka(1423/23+3_124, 183*233/123-43+true);
#                 }
#                 jesus(true);
#             }
#         }
#         """
#         expect = """Program([\n\tVarDecl(huy_12, FloatType, FloatLit(0.0))\n\tVarDecl(__, BooleanType, BooleanLit(True))\n\tFuncDecl(_291, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(ArrayCell(a, [ArrayCell(a, [ArrayCell(a, [IntegerLit(2910), IntegerLit(989)])])]), BooleanLit(True)), BinExpr(<, Id(hey), BinExpr(+, Id(hey), UnExpr(-, UnExpr(-, UnExpr(-, IntegerLit(2)))))), BinExpr(-, Id(hi), UnExpr(-, IntegerLit(2))), BlockStmt([ForStmt(AssignStmt(ArrayCell(a, [IntegerLit(304)]), FuncCall(foo, [BinExpr(*, IntegerLit(2), IntegerLit(3))])), BinExpr(<, Id(i), IntegerLit(1)), BinExpr(-, Id(i), UnExpr(-, IntegerLit(2))), BlockStmt([CallStmt(saka, BinExpr(+, BinExpr(/, IntegerLit(1423), IntegerLit(23)), IntegerLit(3124)), BinExpr(+, BinExpr(-, BinExpr(/, BinExpr(*, IntegerLit(183), IntegerLit(233)), IntegerLit(123)), IntegerLit(43)), BooleanLit(True)))])), CallStmt(jesus, BooleanLit(True))]))]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 356))
#     def test_57(self):
#         """test 57"""
#         input = """
#         hi: integer;
#         main: function void()
#         {
#             if (!- huy + quan/2 + -hi){
#                 return huy(29+10/2*32);
#             }
#             if (true){
#                 return "huy ham hoc";
#             }
#             else{
#                 while(true){
#                     a = a + --21/42 % "huy";
#                 }
#             }
#         }
#         """
#         expect = """Program([\n\tVarDecl(hi, IntegerType)\n\tFuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(+, BinExpr(+, UnExpr(!, UnExpr(-, Id(huy))), BinExpr(/, Id(quan), IntegerLit(2))), UnExpr(-, Id(hi))), BlockStmt([ReturnStmt(FuncCall(huy, [BinExpr(+, IntegerLit(29), BinExpr(*, BinExpr(/, IntegerLit(10), IntegerLit(2)), IntegerLit(32)))]))])), IfStmt(BooleanLit(True), BlockStmt([ReturnStmt(StringLit(huy ham hoc))]), BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), BinExpr(%, BinExpr(/, UnExpr(-, UnExpr(-, IntegerLit(21))), IntegerLit(42)), StringLit(huy))))]))]))]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 357))
#     def test_58(self):
#         """test 58"""
#         input = """
#         hi: integer;
#         main: function void() inherit a_29
#         {
#             do{
#                 b = a::a;
#                 a[a[123_23, 32_21]] = "hello";
#                 while (false){
#                     saygoodbye();
#                 }
#             }
#             while (huy < huy +1.e-2-31/4%!true);
#         }
#         """
#         expect = """Program([\n\tVarDecl(hi, IntegerType)\n\tFuncDecl(main, VoidType, [], a_29, BlockStmt([DoWhileStmt(BinExpr(<, Id(huy), BinExpr(-, BinExpr(+, Id(huy), FloatLit(0.01)), BinExpr(%, BinExpr(/, IntegerLit(31), IntegerLit(4)), UnExpr(!, BooleanLit(True))))), BlockStmt([AssignStmt(Id(b), BinExpr(::, Id(a), Id(a))), AssignStmt(ArrayCell(a, [ArrayCell(a, [IntegerLit(12323), IntegerLit(3221)])]), StringLit(hello)), WhileStmt(BooleanLit(False), BlockStmt([CallStmt(saygoodbye, )]))]))]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 358))
#     def test_59(self):
#         input = """
#             huy_29,quan_27: integer = (!(huy||quan)&&c||!("bye"))==false, ((quan+((-((huy()+-d_12[29_10, 21_0]))))));
#         """
#         expect = """Program([\n\tVarDecl(huy_29, IntegerType, BinExpr(==, BinExpr(||, BinExpr(&&, UnExpr(!, BinExpr(||, Id(huy), Id(quan))), Id(c)), UnExpr(!, StringLit(bye))), BooleanLit(False)))\n\tVarDecl(quan_27, IntegerType, BinExpr(+, Id(quan), UnExpr(-, BinExpr(+, FuncCall(huy, []), UnExpr(-, ArrayCell(d_12, [IntegerLit(2910), IntegerLit(210)]))))))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 359))
#     def test60(self):
#             """test 60"""
#             input = """
#         thien: integer = 123_21.e+23;
#         wee_542_pe: float = .e-294;
#         main: function void(){
#             if (thien != 2334_72987 && (pe == "pe cham chi pe ham hoc"))
#             {
#                 for (thien_29_3728 = 38*28/323+12.23e2, thien < "thien 10 diem", a - thien + pe/29)
#                 {
#                     thien = 1;
#                 }
#                 for (m=1_234_1_294, m < 1223_2_2_42, m + 2345e+2)
#                 {
#                     testcase(10*2);
#                     if (sdjsfds==2)
#                     {
#                         h,a,d: integer = 123_23,1_4_8_9_0,29_1_0;
#                     }
#                 }

#             }
#             thao(2/3+1*2*2+pe);
#         }
# """
#             expect = """Program([\n\tVarDecl(thien, IntegerType, FloatLit(1.2321e+27))\n\tVarDecl(wee_542_pe, FloatType, FloatLit(0.0))\n\tFuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(!=, Id(thien), BinExpr(&&, IntegerLit(233472987), BinExpr(==, Id(pe), StringLit(pe cham chi pe ham hoc)))), BlockStmt([ForStmt(AssignStmt(Id(thien_29_3728), BinExpr(+, BinExpr(/, BinExpr(*, IntegerLit(38), IntegerLit(28)), IntegerLit(323)), FloatLit(1223.0))), BinExpr(<, Id(thien), StringLit(thien 10 diem)), BinExpr(+, BinExpr(-, Id(a), Id(thien)), BinExpr(/, Id(pe), IntegerLit(29))), BlockStmt([AssignStmt(Id(thien), IntegerLit(1))])), ForStmt(AssignStmt(Id(m), IntegerLit(12341294)), BinExpr(<, Id(m), IntegerLit(12232242)), BinExpr(+, Id(m), FloatLit(234500.0)), BlockStmt([CallStmt(testcase, BinExpr(*, IntegerLit(10), IntegerLit(2))), IfStmt(BinExpr(==, Id(sdjsfds), IntegerLit(2)), BlockStmt([VarDecl(h, IntegerType, IntegerLit(12323)), VarDecl(a, IntegerType, IntegerLit(14890)), VarDecl(d, IntegerType, IntegerLit(2910))]))]))])), CallStmt(thao, BinExpr(+, BinExpr(+, BinExpr(/, IntegerLit(2), IntegerLit(3)), BinExpr(*, BinExpr(*, IntegerLit(1), IntegerLit(2)), IntegerLit(2))), Id(pe)))]))\n])"""
#             self.assertTrue(TestAST.test(input, expect, 360))
#     def test_61(self):
#         """test 61"""
#         input = """huy,ca,da: boolean = "true", "false", true; """
#         expect = """Program([\n\tVarDecl(huy, BooleanType, StringLit(true))\n\tVarDecl(ca, BooleanType, StringLit(false))\n\tVarDecl(da, BooleanType, BooleanLit(True))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 361))

#     def test_62(self):
#         """test 62"""
#         input = """lam,huy,quan,fuong,gio: float = 1_29_549_29.e-2, 2_29_10, 1_2.42e-5, quan_ham_2710, true; """
#         expect = """Program([\n\tVarDecl(lam, FloatType, FloatLit(129549.29))\n\tVarDecl(huy, FloatType, IntegerLit(22910))\n\tVarDecl(quan, FloatType, FloatLit(0.0001242))\n\tVarDecl(fuong, FloatType, Id(quan_ham_2710))\n\tVarDecl(gio, FloatType, BooleanLit(True))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 362))
#     def test_63(self):
#         """test 63"""
#         input = """__06: array [2_21,3_3_12_123] of boolean;quanvahuy: integer = "quan ham hoc"; """
#         expect = """Program([\n\tVarDecl(__06, ArrayType([221, 3312123], BooleanType))\n\tVarDecl(quanvahuy, IntegerType, StringLit(quan ham hoc))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 363))
#     def test_64(self):
#         """test 64"""
#         input = """saka, antony: boolean = super[24,4_4], hero[2_12,7_42]; """
#         expect = """Program([\n\tVarDecl(saka, BooleanType, ArrayCell(super, [IntegerLit(24), IntegerLit(44)]))\n\tVarDecl(antony, BooleanType, ArrayCell(hero, [IntegerLit(212), IntegerLit(742)]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 364))
#     def test_65(self):
#         """test 65"""
#         input = """huy, cfh, tulia: string = messi(22_12), ba[29], quan_dep_trai ; /* day chi la test */"""
#         expect = """Program([\n\tVarDecl(huy, StringType, FuncCall(messi, [IntegerLit(2212)]))\n\tVarDecl(cfh, StringType, ArrayCell(ba, [IntegerLit(29)]))\n\tVarDecl(tulia, StringType, Id(quan_dep_trai))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 365))
#     def test_66(self):
#         """test 66"""
#         input = """qu_27, h_29, t_31: integer = false, true, "quan di choi \\t"; // dang alm test case"""
#         expect = """Program([\n\tVarDecl(qu_27, IntegerType, BooleanLit(False))\n\tVarDecl(h_29, IntegerType, BooleanLit(True))\n\tVarDecl(t_31, IntegerType, StringLit(quan di choi \\t))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 366))
#     def test_67(self):
#         """test 67"""
#         input = """ma_06, ba_29, ac_03: integer = huy_09, 24_06_03_29, {3_1, 9.e-1}; // dang alm test case"""
#         expect = """Program([\n\tVarDecl(ma_06, IntegerType, Id(huy_09))\n\tVarDecl(ba_29, IntegerType, IntegerLit(24060329))\n\tVarDecl(ac_03, IntegerType, ArrayLit([IntegerLit(31), FloatLit(0.9)]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 367))
#     def test_68(self):
#         """test 68"""
#         input = """huy, lst, u_an: boolean = true,true, false;"""
#         expect = """Program([\n\tVarDecl(huy, BooleanType, BooleanLit(True))\n\tVarDecl(lst, BooleanType, BooleanLit(True))\n\tVarDecl(u_an, BooleanType, BooleanLit(False))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 368))
#     def test_69(self):
#         """test 69"""
#         input = """h_uy, _foo_1, trung_0101: float = 32_9_10.2100, uy[2_9_2_29, 9_0_11], {9_12_43_0, 22_90} ;
#                     a_bc_d, d_huy: string ;"""
#         expect = """Program([\n\tVarDecl(h_uy, FloatType, FloatLit(32910.21))\n\tVarDecl(_foo_1, FloatType, ArrayCell(uy, [IntegerLit(29229), IntegerLit(9011)]))\n\tVarDecl(trung_0101, FloatType, ArrayLit([IntegerLit(912430), IntegerLit(2290)]))\n\tVarDecl(a_bc_d, StringType)\n\tVarDecl(d_huy, StringType)\n])"""
#         self.assertTrue(TestAST.test(input, expect, 369))
#     def test_70(self):
#         """test 70"""
#         input = """huy_2_9: array [2_29, 2_9_0_6, 12_1_2_12_3_3] of boolean;
#                     a_29 : string = {"quan", "huy","thanh", "cuong"} ;
#                     t_anh: integer = {12.e+10, 1_2.10, 29_10.e3}; """
#         expect = """Program([\n\tVarDecl(huy_2_9, ArrayType([229, 2906, 12121233], BooleanType))\n\tVarDecl(a_29, StringType, ArrayLit([StringLit(quan), StringLit(huy), StringLit(thanh), StringLit(cuong)]))\n\tVarDecl(t_anh, IntegerType, ArrayLit([FloatLit(120000000000.0), FloatLit(12.1), FloatLit(2910000.0)]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 370))
#     def test_71(self):
#         """test 71"""
#         input = """lost_first: array [1_0_19, 2_10, 2_22] of integer = a1_0[19_20, "hello huy \\"huy khoe khong\\"", false, false, 1_29_1.21, 2_9_3_1_12];
#                     hi : string = {12_21, "huy dang lam bai", false, 1.e-1} ;
#                     hello: float = {12.e+10, "quan lam bai \\f"}; """
#         expect = """Program([\n\tVarDecl(lost_first, ArrayType([1019, 210, 222], IntegerType), ArrayCell(a1_0, [IntegerLit(1920), StringLit(hello huy \\"huy khoe khong\\"), BooleanLit(False), BooleanLit(False), FloatLit(1291.21), IntegerLit(293112)]))\n\tVarDecl(hi, StringType, ArrayLit([IntegerLit(1221), StringLit(huy dang lam bai), BooleanLit(False), FloatLit(0.1)]))\n\tVarDecl(hello, FloatType, ArrayLit([FloatLit(120000000000.0), StringLit(quan lam bai \\f)]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 371))
#     def test_72(self):
#         """test 72"""
#         input = """lost_her, a_06_06, d_2_03: float = foo(2+x, 4/y), a+10/2, b_102 || 29 ; """
#         expect = """Program([\n\tVarDecl(lost_her, FloatType, FuncCall(foo, [BinExpr(+, IntegerLit(2), Id(x)), BinExpr(/, IntegerLit(4), Id(y))]))\n\tVarDecl(a_06_06, FloatType, BinExpr(+, Id(a), BinExpr(/, IntegerLit(10), IntegerLit(2))))\n\tVarDecl(d_2_03, FloatType, BinExpr(||, Id(b_102), IntegerLit(29)))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 372))
#     def test_73(self):
#         """test 73"""
#         input = """_quan, lam_09, huy_29: boolean = m_12_01(2_123_1::x), !1.e1, -2_12e-2 ; """
#         expect = """Program([\n\tVarDecl(_quan, BooleanType, FuncCall(m_12_01, [BinExpr(::, IntegerLit(21231), Id(x))]))\n\tVarDecl(lam_09, BooleanType, UnExpr(!, FloatLit(10.0)))\n\tVarDecl(huy_29, BooleanType, UnExpr(-, FloatLit(2.12)))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 373))
#     def test_74(self):
#         """test 74"""
#         input = """huy_quan, _18_08 : array [4_1_0_1] of string  = "quan \\b" != "huy \\f", 3_1_1_12_123 > 4_12_3 ; """
#         expect = """Program([\n\tVarDecl(huy_quan, ArrayType([4101], StringType), BinExpr(!=, StringLit(quan \\b), StringLit(huy \\f)))\n\tVarDecl(_18_08, ArrayType([4101], StringType), BinExpr(>, IntegerLit(31112123), IntegerLit(4123)))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 374))
#     def test_75(self):
#         """test 75"""
#         input = """saka_jesus, quy_18 : float  = {true,false,true,false}, 2_12_12 <= 4_111_29 ;
#                     a,b:  float = 1_02.2e-1 >= 1_01.3e-3, a+10/2*3.e1-x_29 ;"""
#         expect = """Program([\n\tVarDecl(saka_jesus, FloatType, ArrayLit([BooleanLit(True), BooleanLit(False), BooleanLit(True), BooleanLit(False)]))\n\tVarDecl(quy_18, FloatType, BinExpr(<=, IntegerLit(21212), IntegerLit(411129)))\n\tVarDecl(a, FloatType, BinExpr(>=, FloatLit(10.22), FloatLit(0.1013)))\n\tVarDecl(b, FloatType, BinExpr(-, BinExpr(+, Id(a), BinExpr(*, BinExpr(/, IntegerLit(10), IntegerLit(2)), FloatLit(30.0))), Id(x_29)))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 375))
#     def test_76(self):
#         """test 76"""
#         input = """uy_01_1, si : string  = 2_12 +- 5_1_1_02, !29%5 ;
#                     a,b:  string = "huy \\"dang hoc\\" bi quan pha ", "quan bip bom"=="huy that tha" ;"""
#         expect = """Program([\n\tVarDecl(uy_01_1, StringType, BinExpr(+, IntegerLit(212), UnExpr(-, IntegerLit(51102))))\n\tVarDecl(si, StringType, BinExpr(%, UnExpr(!, IntegerLit(29)), IntegerLit(5)))\n\tVarDecl(a, StringType, StringLit(huy \\"dang hoc\\" bi quan pha ))\n\tVarDecl(b, StringType, BinExpr(==, StringLit(quan bip bom), StringLit(huy that tha)))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 376))
#     def test_77(self):
#         """test 77"""
#         input = """quang_huy : array[1_23,2_21] of float = {"huy dang hoc", "huy co gang \\"hoc that tot \\t\\""}  ;
#                     c,d:  integer = 12_102 -- 29_1_9_0, quan[23_12, 32_1_2_06] ;"""
#         expect = """Program([\n\tVarDecl(quang_huy, ArrayType([123, 221], FloatType), ArrayLit([StringLit(huy dang hoc), StringLit(huy co gang \\"hoc that tot \\t\\")]))\n\tVarDecl(c, IntegerType, BinExpr(-, IntegerLit(12102), UnExpr(-, IntegerLit(29190))))\n\tVarDecl(d, IntegerType, ArrayCell(quan, [IntegerLit(2312), IntegerLit(321206)]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 377))
#     def test_78(self):
#         """test 78"""
#         input = """h_29_10 : integer = -3+29*9/10+4 ;
#                     a, c: float = !12.e3, quan || huy && thanh   ;
#                     f_1 : array[234_1,2_305,21_9,32_2] of float; """
#         expect = """Program([\n\tVarDecl(h_29_10, IntegerType, BinExpr(+, BinExpr(+, UnExpr(-, IntegerLit(3)), BinExpr(/, BinExpr(*, IntegerLit(29), IntegerLit(9)), IntegerLit(10))), IntegerLit(4)))\n\tVarDecl(a, FloatType, UnExpr(!, FloatLit(12000.0)))\n\tVarDecl(c, FloatType, BinExpr(&&, BinExpr(||, Id(quan), Id(huy)), Id(thanh)))\n\tVarDecl(f_1, ArrayType([2341, 2305, 219, 322], FloatType))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 378))
#     def test_79(self):
#         """test 79"""
#         input = """ quan: float = "huy dang hoc \\f\\t" :: "huy chay deadline" == "quan choi game" ;
#                      """
#         expect = """Program([\n\tVarDecl(quan, FloatType, BinExpr(::, StringLit(huy dang hoc \\f\\t), BinExpr(==, StringLit(huy chay deadline), StringLit(quan choi game))))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 379))
#     def test_80(self):
#         """test 80"""
#         input = """ huy: integer = __huy(2_12*me(1.23+2_1.e1/12_02*12--12)) ;
#                     _09_10,h,u,y: integer = true,false,hello,2.3e+1;
#                     c_1808: float;
#                      """
#         expect = """Program([\n\tVarDecl(huy, IntegerType, FuncCall(__huy, [BinExpr(*, IntegerLit(212), FuncCall(me, [BinExpr(-, BinExpr(+, FloatLit(1.23), BinExpr(*, BinExpr(/, FloatLit(210.0), IntegerLit(1202)), IntegerLit(12))), UnExpr(-, IntegerLit(12)))]))]))\n\tVarDecl(_09_10, IntegerType, BooleanLit(True))\n\tVarDecl(h, IntegerType, BooleanLit(False))\n\tVarDecl(u, IntegerType, Id(hello))\n\tVarDecl(y, IntegerType, FloatLit(23.0))\n\tVarDecl(c_1808, FloatType)\n])"""
#         self.assertTrue(TestAST.test(input, expect, 380))
#     def test_81(self):
#         """test 81"""
#         input = """ _10_huy: float = {"huy", "huy dang lam testcase \\t\\f"};
#                     _baba_2404: integer = !-12*23+3*4 ;
#                      """
#         expect = """Program([\n\tVarDecl(_10_huy, FloatType, ArrayLit([StringLit(huy), StringLit(huy dang lam testcase \\t\\f)]))\n\tVarDecl(_baba_2404, IntegerType, BinExpr(+, BinExpr(*, UnExpr(!, UnExpr(-, IntegerLit(12))), IntegerLit(23)), BinExpr(*, IntegerLit(3), IntegerLit(4))))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 381))
#     def test_82(self):
#         """test 82"""
#         input = """ mami_06: float = {"huy", "huy dang di hoc \\b\\n"};
#                     baba: boolean = !-12*23+3*4 ;
#                      """
#         expect = """Program([\n\tVarDecl(mami_06, FloatType, ArrayLit([StringLit(huy), StringLit(huy dang di hoc \\b\\n)]))\n\tVarDecl(baba, BooleanType, BinExpr(+, BinExpr(*, UnExpr(!, UnExpr(-, IntegerLit(12))), IntegerLit(23)), BinExpr(*, IntegerLit(3), IntegerLit(4))))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 382))
#     def test_83(self):
#         """test 83"""
#         input = """ ma_6: float = 12321.2e1+1_123--3_21*1.2e+1;
#                     baba_4: integer = "huy dang lam test case \\f\\"dung lam phien huy\\t\\"";
#                      """
#         expect = """Program([\n\tVarDecl(ma_6, FloatType, BinExpr(-, BinExpr(+, FloatLit(123212.0), IntegerLit(1123)), BinExpr(*, UnExpr(-, IntegerLit(321)), FloatLit(12.0))))\n\tVarDecl(baba_4, IntegerType, StringLit(huy dang lam test case \\f\\"dung lam phien huy\\t\\"))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 383))
#     def test_84(self):
#         """test 84"""
#         input = """ _huy9, che_03: array [1_2, 2_13, 4_12] of float = !-1_234e+1-24_123/1_11, {huy, true, 2_123.23, 1_032, "quan coc huy \\b\\"huy khoc \\f\\""};
#                      """
#         expect = """Program([\n\tVarDecl(_huy9, ArrayType([12, 213, 412], FloatType), BinExpr(-, UnExpr(!, UnExpr(-, FloatLit(12340.0))), BinExpr(/, IntegerLit(24123), IntegerLit(111))))\n\tVarDecl(che_03, ArrayType([12, 213, 412], FloatType), ArrayLit([Id(huy), BooleanLit(True), FloatLit(2123.23), IntegerLit(1032), StringLit(quan coc huy \\b\\"huy khoc \\f\\")]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 384))
#     def test_85(self):
#         """test 85"""
#         input = """ quan, h_10_, lamf_1: string = "quan" :: "huy dang hoc \\f" < "thanh cay phim" || hello_friend, !-1234.23e-1, messi(2_12/x) ;
#                      """
#         expect = """Program([\n\tVarDecl(quan, StringType, BinExpr(::, StringLit(quan), BinExpr(<, StringLit(huy dang hoc \\f), BinExpr(||, StringLit(thanh cay phim), Id(hello_friend)))))\n\tVarDecl(h_10_, StringType, UnExpr(!, UnExpr(-, FloatLit(123.423))))\n\tVarDecl(lamf_1, StringType, FuncCall(messi, [BinExpr(/, IntegerLit(212), Id(x))]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 385))
#     def test_86(self):
#         """test 86"""
#         input = """ lam_09, thanh_10: integer = 123_123_1_0_1_12, 2910.2e-1 ;
#                     a,c,d: float; """
#         expect = """Program([\n\tVarDecl(lam_09, IntegerType, IntegerLit(12312310112))\n\tVarDecl(thanh_10, IntegerType, FloatLit(291.02))\n\tVarDecl(a, FloatType)\n\tVarDecl(c, FloatType)\n\tVarDecl(d, FloatType)\n])"""
#         self.assertTrue(TestAST.test(input, expect, 386))
#     def test_87(self):
#         """test 87"""
#         input = """ba_24: function auto (a: integer, b: string, e: boolean){
#         } """
#         expect = """Program([\n\tFuncDecl(ba_24, AutoType, [Param(a, IntegerType), Param(b, StringType), Param(e, BooleanType)], None, BlockStmt([]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 387))
#     def test_88(self):
#         """test 88"""
#         input = """cau_03: function void (a: integer, b: string, e: boolean){
#             saka();
#         } """
#         expect = """Program([\n\tFuncDecl(cau_03, VoidType, [Param(a, IntegerType), Param(b, StringType), Param(e, BooleanType)], None, BlockStmt([CallStmt(saka, )]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 388))
#     def test_89(self):
#         """test 89"""
#         input = """huy: function auto (out a: integer, delta: integer){
#             n = n + delta;
#         } """
#         expect = """Program([\n\tFuncDecl(huy, AutoType, [OutParam(a, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 389))
#     def test_90(self):
#         """test 90"""
#         input = """huy_29: function string (inherit out huy_29: string, out _h__: float, __: integer) inherit quan_thay{
#             if (a == 1)
#                 return a;
#         } """
#         expect = """Program([\n\tFuncDecl(huy_29, StringType, [InheritOutParam(huy_29, StringType), OutParam(_h__, FloatType), Param(__, IntegerType)], quan_thay, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), ReturnStmt(Id(a)))]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 390))
#     def test_91(self):
#         """test 91"""
#         input = """x : integer=65;
#         food : function string(n : integer) {
#         if ( n == 0 ) return 1 ;
#         else return n * fact(n - 1 ) ;
#         }
#         drink : function auto (out n : integer , delta : integer) {
#         n = n + delta ;
#         }
#         main : function void () {
#         delta : integer = fact(3) ;
#         inc(x ,delta ) ;
#         printInteger(x) ;
#         }
#         """
#         expect = """Program([\n\tVarDecl(x, IntegerType, IntegerLit(65))\n\tFuncDecl(food, StringType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))\n\tFuncDecl(drink, AutoType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))\n\tFuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)])), CallStmt(inc, Id(x), Id(delta)), CallStmt(printInteger, Id(x))]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 391))
#     def test_92(self):
#         """test 92"""
#         input = """baba: function integer () {
#         d: integer = 49_03;
#         }"""
#         expect = """Program([\n\tFuncDecl(baba, IntegerType, [], None, BlockStmt([VarDecl(d, IntegerType, IntegerLit(4903))]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 392))
#     def test_93(self):
#         """test 93"""
#         input = """quan_02: function array[1_22_123_1] of integer (inherit yeu_29: array[52_12, 1_2] of string, out _: integer, d_12: boolean) {
#         for (i = 1, i < 10, i + 1) {
#             sayhi(hello);
#             }
#         }"""
#         expect = """Program([\n\tFuncDecl(quan_02, ArrayType([1221231], IntegerType), [InheritParam(yeu_29, ArrayType([5212, 12], StringType)), OutParam(_, IntegerType), Param(d_12, BooleanType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(sayhi, Id(hello))]))]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 393))
#     def test_94(self):
#         """test 94"""
#         input = """hello: function string (inherit out a: integer, out b29: string) inherit function_name{
#             d_29, h_9: integer = true, 12.31e+1;
#             do {
#                 r, s: integer;
#                 r = 2.0;
#                 a, b: array [5] of integer;
#                 s = r * r * myPI;
#                 a[0] = s;
#                 }
#             while ("huy" != "lam" );
#             }"""
#         expect = """Program([\n\tFuncDecl(hello, StringType, [InheritOutParam(a, IntegerType), OutParam(b29, StringType)], function_name, BlockStmt([VarDecl(d_29, IntegerType, BooleanLit(True)), VarDecl(h_9, IntegerType, FloatLit(123.1)), DoWhileStmt(BinExpr(!=, StringLit(huy), StringLit(lam)), BlockStmt([VarDecl(r, IntegerType), VarDecl(s, IntegerType), AssignStmt(Id(r), FloatLit(2.0)), VarDecl(a, ArrayType([5], IntegerType)), VarDecl(b, ArrayType([5], IntegerType)), AssignStmt(Id(s), BinExpr(*, BinExpr(*, Id(r), Id(r)), Id(myPI))), AssignStmt(ArrayCell(a, [IntegerLit(0)]), Id(s))]))]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 394))
#     def test_95(self):
#         """test 95"""
#         input = """
#         /* Huy chua co bo */
#         b, c : float = !true, "false";
#         part: function auto (out n: integer,inherit i: string) inherit foo {
#             /* dang lam testcase */
#             for (a[a[0, 1_2]] = 0, (a < 1_0.20) || !false, a*-2) x = x*(2+y);
#         }
#         """
#         expect = """Program([\n\tVarDecl(b, FloatType, UnExpr(!, BooleanLit(True)))\n\tVarDecl(c, FloatType, StringLit(false))\n\tFuncDecl(part, AutoType, [OutParam(n, IntegerType), InheritParam(i, StringType)], foo, BlockStmt([ForStmt(AssignStmt(ArrayCell(a, [ArrayCell(a, [IntegerLit(0), IntegerLit(12)])]), IntegerLit(0)), BinExpr(||, BinExpr(<, Id(a), FloatLit(10.2)), UnExpr(!, BooleanLit(False))), BinExpr(*, Id(a), UnExpr(-, IntegerLit(2))), AssignStmt(Id(x), BinExpr(*, Id(x), BinExpr(+, IntegerLit(2), Id(y)))))]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 395))
#     def test_96(self):
#         """test 96"""
#         input = """
#             a, b, c: string = "hello\\"Quynh Lam\\"\\t ne", 1_23_45.21000, foo(bar(), a);
#             t: array [1_0, 2_0] of string = {"\\"Lam khong yeu Huy\\""};
#             func: function void (inherit out x: array [0, 1] of boolean, out i: string) {
#                 {
#                     // Empty block
#                 }
#                 {
#                     /* Empty block */
#                     {
#                         print("Hello");
#                     }
#                 }
#             }
#         """
#         expect = """Program([\n\tVarDecl(a, StringType, StringLit(hello\\"Quynh Lam\\"\\t ne))\n\tVarDecl(b, StringType, FloatLit(12345.21))\n\tVarDecl(c, StringType, FuncCall(foo, [FuncCall(bar, []), Id(a)]))\n\tVarDecl(t, ArrayType([10, 20], StringType), ArrayLit([StringLit(\\"Lam khong yeu Huy\\")]))\n\tFuncDecl(func, VoidType, [InheritOutParam(x, ArrayType([0, 1], BooleanType)), OutParam(i, StringType)], None, BlockStmt([BlockStmt([]), BlockStmt([BlockStmt([CallStmt(print, StringLit(Hello))])])]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 396))
#     def test_97(self):
#         """test 97"""
#         input = """huy, quan: array[12_1,21_3] of integer= {"quan luot tiktok \\"ko trl tin nhan nhi\\"", "nhi buon nhi khoc"}, 123_12.e+3;
#                 friend_29: function void (inherit b: integer, out a: string) inherit quandeptrai{
#                 while (a < a+1)
#                  a[213, 3_12] = 29;
#                  break;
#                 } """
#         expect = """Program([\n\tVarDecl(huy, ArrayType([121, 213], IntegerType), ArrayLit([StringLit(quan luot tiktok \\"ko trl tin nhan nhi\\"), StringLit(nhi buon nhi khoc)]))\n\tVarDecl(quan, ArrayType([121, 213], IntegerType), FloatLit(12312000.0))\n\tFuncDecl(friend_29, VoidType, [InheritParam(b, IntegerType), OutParam(a, StringType)], quandeptrai, BlockStmt([WhileStmt(BinExpr(<, Id(a), BinExpr(+, Id(a), IntegerLit(1))), AssignStmt(ArrayCell(a, [IntegerLit(213), IntegerLit(312)]), IntegerLit(29))), BreakStmt()]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 397))
#     def test_98(self):
#         """test 98"""
#         input = """quan, huy2_9_10: float= {"quan con choi insta ko", hello, 12_2_9_0_1_123, 1_2.e-1}, foo(2/x);
#                 main: function string (inherit a_29: string, out quan__27: array[2_1] of boolean) inherit lam_testcae {
#                     if (a != 23)
#                         return foo(4+y);
                    
#                     else{
#                         messi(2+x/y*3);
#                         continue;
#                     }
#                 }  """
#         expect = """Program([\n\tVarDecl(quan, FloatType, ArrayLit([StringLit(quan con choi insta ko), Id(hello), IntegerLit(122901123), FloatLit(1.2)]))\n\tVarDecl(huy2_9_10, FloatType, FuncCall(foo, [BinExpr(/, IntegerLit(2), Id(x))]))\n\tFuncDecl(main, StringType, [InheritParam(a_29, StringType), OutParam(quan__27, ArrayType([21], BooleanType))], lam_testcae, BlockStmt([IfStmt(BinExpr(!=, Id(a), IntegerLit(23)), ReturnStmt(FuncCall(foo, [BinExpr(+, IntegerLit(4), Id(y))])), BlockStmt([CallStmt(messi, BinExpr(+, IntegerLit(2), BinExpr(*, BinExpr(/, Id(x), Id(y)), IntegerLit(3)))), ContinueStmt()]))]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 398))
#     def test_99(self):
#         """test 99"""
#         input = """
#                 fat: function auto (inherit a_29: string, out quan__27: array[2_1] of boolean) inherit lam_testcae {
#                     hi_huy: integer = {"quan luot tiktok"};
#                     for (i = 1, i < 2,  x+y*z/t+--2_3){
#                         for (a[21,12_2_0] = 2, a < 12.e+1, a+1)
#                         {
#                             return;
#                         }
#                         i = i+1;
#                     }
#                 }  """
#         expect = """Program([\n\tFuncDecl(fat, AutoType, [InheritParam(a_29, StringType), OutParam(quan__27, ArrayType([21], BooleanType))], lam_testcae, BlockStmt([VarDecl(hi_huy, IntegerType, ArrayLit([StringLit(quan luot tiktok)])), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(2)), BinExpr(+, BinExpr(+, Id(x), BinExpr(/, BinExpr(*, Id(y), Id(z)), Id(t))), UnExpr(-, UnExpr(-, IntegerLit(23)))), BlockStmt([ForStmt(AssignStmt(ArrayCell(a, [IntegerLit(21), IntegerLit(1220)]), IntegerLit(2)), BinExpr(<, Id(a), FloatLit(120.0)), BinExpr(+, Id(a), IntegerLit(1)), BlockStmt([ReturnStmt()])), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 399))
#     def test_100(self):
#         """test 100"""
#         input = """huy_29_10: string = !!- aaa;
#         thanh_19: function float () {
#         while (i < 1)
#             i = i+1;
#         }  """
#         expect = """Program([\n\tVarDecl(huy_29_10, StringType, UnExpr(!, UnExpr(!, UnExpr(-, Id(aaa)))))\n\tFuncDecl(thanh_19, FloatType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(i), IntegerLit(1)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))))]))\n])"""
#         self.assertTrue(TestAST.test(input, expect, 400))
    # def test_100(self):
    #     """test 100"""
    #     input = """a: integer;
    #     a: string;  """
    #     expect = """Program([\n\tVarDecl(a, IntegerType)\n\tVarDecl(a, StringType)\n])"""
    #     self.assertTrue(TestAST.test(input, expect, 401))

    def test_7(self):
        """test 7"""
        input = """a: integer;
                    a: string;
                    foo: function integer(a: integer, d: string){
                        if (n == 0) return 1;
                    }
                   bar: function string(a: integer){
                    return a;
                   }
                    """
        expect = "Type mismatch in Variable Declaration: VarDecl(c, IntegerType, FloatLit(2.1))"
        self.assertTrue(TestAST.test(input, expect, 402))

    