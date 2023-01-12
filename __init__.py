import numpy as np
import random


class Ham_so:

    def __init__(self, difficulty=1):
        self.__meomeo = None
        self.__difficulty = difficulty
        self.__func = self._create_func(difficulty)

    def val(self, x):
        plat_func, plat_derived_func = self.__func
        plat_func_x = [x**i for i in range(len(plat_func)-1, -1, -1)]

        plat_func_y = 0
        plat_derived_func_y = 0

        for i in range(len(plat_func_x)-1):
            plat_func_y += plat_func[i]*plat_func_x[i]
            plat_derived_func_y += plat_derived_func[i] * \
                plat_func_x[i+1]
        plat_func_y += plat_func[-1]
        return plat_func_y, plat_derived_func_y

    def __ConMeoDeThuong(self, p1, p2):
        conga = p2+[0]*(len(p1)-1)
        col = len(conga)
        row = len(p1)
        arr = np.array((conga+[0])*(row-1)+p2)
        matrix = arr.reshape(row, col)
        product_of_two = np.array(p1).dot(matrix)
        return product_of_two.astype(float)

    def _create_func(self, difficulty):
        coef_derived = [[1, random.randint(-100, 100)]
                        for i in range(random.randint(difficulty-1, difficulty+1)*2+1)]
        self.__meomeo = [i[1] for i in coef_derived]
        plat_derived_func = self.__ConGaMaiDau(coef_derived)
        plat_func = self.__ConChoCon(plat_derived_func)
        return [plat_func, plat_derived_func]

    def __ConChoCon(self, coef_derived):
        coef_plat = np.copy(coef_derived)
        for i in range(len(coef_derived), 0, -1):
            coef_plat[-i] /= i
        coef_plat = np.concatenate(
            (coef_plat, [random.randint(-10, 10)]))
        return coef_plat

    def __ConGaMaiDau(self, coef_express):

        conmeo = [np.array([1])]
        for factor in coef_express:
            conmeo.append(self.__ConMeoDeThuong(
                conmeo[-1], factor))
        return conmeo[-1]

    def __conmeo(self):
        return min(self.val(-i)[0] for i in self.__meomeo)

    def check(self, x):
        if abs(list(self.val(x))[0] - self.__conmeo) <= 2 * self.__difficulty:
            return True
        return False

