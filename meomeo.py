__version__ = 1.2
import numpy as np
import random
# from typing import


class Ham_so:

    def __init__(self, difficulty=1):

        self.__meomeo = None
        self.__difficulty = difficulty
        self.checkError()

        self.__func = self.__create_func(difficulty)
        self.__y_min, self.__x_min = self.__conmeo()

    def val(self, x):

        plat_func, plat_derived_func = self.__func
        plat_func_x = np.array([pow(x, i)
                               for i in range(len(plat_func)-1, -1, -1)])

        plat_func_y = plat_func @ plat_func_x
        plat_derived_func_y = plat_derived_func @ plat_func_x[1:]

        return plat_func_y, plat_derived_func_y

    def __ConMeoDeThuong(self, p1, p2):

        ConGa = p2+[0]*(len(p1)-1)
        col = len(ConGa)
        row = len(p1)
        arr = np.array((ConGa+[0])*(row-1)+p2)
        matrix = arr.reshape(row, col)
        product_of_two = np.array(p1) @ matrix

        return product_of_two.astype(float)

    def __create_func(self, difficulty):

        coef_derived = [[1, random.uniform(-100000, 100000)]
                        for _ in range(random.randint(difficulty-1, difficulty+1)*2+1)]
        self.__meomeo = np.array([-i[1] for i in coef_derived])
        plat_derived_func = self.__ConGaMaiDau(coef_derived)
        plat_func = self.__ConChoCon(plat_derived_func)

        return (plat_func, plat_derived_func)

    def __ConChoCon(self, coef_derived):
        coef_plat = np.copy(coef_derived)
        for i in range(len(coef_derived), 0, -1):
            coef_plat[-i] /= i
        coef_plat = np.concatenate(
            (coef_plat, [random.randint(-20, 20)]))

        return coef_plat

    def __ConGaMaiDau(self, coef_express):
        conmeo = np.array([1])
        for factor in coef_express:
            conmeo = self.__ConMeoDeThuong(
                conmeo, factor)
        return conmeo

    def __conmeo(self):
        value_Y = np.array([self.val(i)[0] for i in self.__meomeo])
        index_Min = np.argmin(value_Y)

        return value_Y[index_Min], self.__meomeo[index_Min]

    def check(self, x):

        if abs(self.val(x)[0] - self.__y_min) <= 2 * self.__difficulty:

            return True

        return False

    def show_min(self):

        print([self.__y_min, self.__x_min])
        exit(0)

    def checkError(self):
        try:
            if self.__difficulty < 1 or self.__difficulty != int(self.__difficulty):
                raise ValueError
        except (ValueError, TypeError):
            print("--Difficulty must be a positive integer--")
            exit(1)
