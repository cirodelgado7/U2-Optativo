from ManejadorProyecto import ManejadorPro
from ManejadorIntegrantes import ManejadorInt

if __name__ == '__main__':
    mp = ManejadorPro()
    mi = ManejadorInt()
    mi.cargarIntegrantes()
    mp.modificarPuntaje(mi)