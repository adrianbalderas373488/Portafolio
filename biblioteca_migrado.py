"""
biblioteca_migrado.py
Migración a Python (POO) del sistema de biblioteca en C.

Características implementadas (requisitos mínimos):
- Clases/objetos para Biblioteca, Usuarios e Ítems (Book, Magazine).
- Herencia: Item (abstracta) -> Book, Magazine.
- Encapsulamiento: atributos privados con getters/setters cuando aplica.
- Abstracción: Item es una clase abstracta con métodos que deben implementarse.
- Polimorfismo: método `display()` sobrescrito en subclases; `to_dict()` polymórfico.
- Registrar ítems/usuarios, préstamos, devoluciones, búsquedas.
- Persistencia simple en JSON (items.json, users.json).
- Interfaz por consola (menú de texto).

Para ejecutar: `python biblioteca_migrado.py`

"""
from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, asdict
from typing import List, Optional, Dict, Any
import json
import os


# -----------------------------
# Clases de dominio (POO)
# -----------------------------
class Item(ABC):
    """Clase abstracta que representa un item genérico en la biblioteca."""

    def __init__(self, item_id: int, title: str, publication_year: Optional[int], quantity: int):
        self._id = item_id
        self._title = title
        self._publication_year = publication_year
        self._quantity = quantity

    @property
    def id(self) -> int:
        return self._id

    @property
    def title(self) -> str:
        return self._title

    @property
    def publication_year(self) -> Optional[int]:
        return self._publication_year

    @property
    def quantity(self) -> int:
        return self._quantity

    def decrement(self) -> bool:
        if self._quantity > 0:
            self._quantity -= 1
            return True
        return False

    def increment(self) -> None:
        self._quantity += 1

    @abstractmethod
    def display(self) -> str:
        """Debe devolver una representación legible del item."""
        raise NotImplementedError

    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def from_dict(data: Dict[str, Any]) -> "Item":
        raise NotImplementedError


class Book(Item):
    def __init__(self, item_id: int, title: str, author: str, publication_year: Optional[int], genre: str, quantity: int):
        super().__init__(item_id, title, publication_year, quantity)
        self._author = author
        self._genre = genre

    @property
    def author(self) -> str:
        return self._author

    @property
    def genre(self) -> str:
        return self._genre

    def display(self) -> str:
        return f"[Libro] ID:{self.id} | {self.title} — {self.author} ({self.publication_year}) | Género: {self.genre} | Cant: {self.quantity}"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "type": "book",
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "publication_year": self.publication_year,
            "genre": self.genre,
            "quantity": self.quantity
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Book":
        return Book(
            item_id=int(data["id"]),
            title=data.get("title", ""),
            author=data.get("author", ""),
            publication_year=data.get("publication_year"),
            genre=data.get("genre", ""),
            quantity=int(data.get("quantity", 0))
        )


class Magazine(Item):
    def __init__(self, item_id: int, title: str, issue: str, publication_year: Optional[int], quantity: int):
        super().__init__(item_id, title, publication_year, quantity)
        self._issue = issue

    @property
    def issue(self) -> str:
        return self._issue

    def display(self) -> str:
        return f"[Revista] ID:{self.id} | {self.title} — Edición: {self.issue} ({self.publication_year}) | Cant: {self.quantity}"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "type": "magazine",
            "id": self.id,
            "title": self.title,
            "issue": self.issue,
            "publication_year": self.publication_year,
            "quantity": self.quantity
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Magazine":
        return Magazine(
            item_id=int(data["id"]),
            title=data.get("title", ""),
            issue=data.get("issue", ""),
            publication_year=data.get("publication_year", ""),
            quantity=int(data.get("quantity", 0))
        )


@dataclass
class User:
    _id: int
    _name: str
    _issued_books: List[int]

    def __init__(self, user_id: int, name: str):
        self._id = user_id
        self._name = name
        self._issued_books = []

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def issued_books(self) -> List[int]:
        return list(self._issued_books)

    def issue(self, item_id: int) -> None:
        self._issued_books.append(item_id)

    def return_item(self, item_id: int) -> bool:
        if item_id in self._issued_books:
            self._issued_books.remove(item_id)
            return True
        return False

    def to_dict(self) -> Dict[str, Any]:
        return {"id": self.id, "name": self.name, "issued_books": self._issued_books}

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "User":
        u = User(int(data["id"]), data.get("name", ""))
        u._issued_books = [int(x) for x in data.get("issued_books", [])]
        return u


# -----------------------------
# Sistema de la biblioteca
# -----------------------------
class LibrarySystem:
    def __init__(self, items_path: str = "items.json", users_path: str = "users.json"):
        self._items_path = items_path
        self._users_path = users_path
        self._items: Dict[int, Item] = {}
        self._users: Dict[int, User] = {}
        self._load()

    # ---------- Persistencia ----------
    def _load(self) -> None:
        # Cargar items
        if os.path.exists(self._items_path):
            try:
                with open(self._items_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                for d in data:
                    t = d.get("type")
                    if t == "book":
                        item = Book.from_dict(d)
                    elif t == "magazine":
                        item = Magazine.from_dict(d)
                    else:
                        continue
                    self._items[item.id] = item
            except Exception as e:
                print(f"Error cargando items: {e}")

        # Cargar usuarios
        if os.path.exists(self._users_path):
            try:
                with open(self._users_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                for d in data:
                    u = User.from_dict(d)
                    self._users[u.id] = u
            except Exception as e:
                print(f"Error cargando usuarios: {e}")

    def save(self) -> None:
        try:
            with open(self._items_path, "w", encoding="utf-8") as f:
                json.dump([it.to_dict() for it in self._items.values()], f, ensure_ascii=False, indent=2)
            with open(self._users_path, "w", encoding="utf-8") as f:
                json.dump([u.to_dict() for u in self._users.values()], f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Error guardando datos: {e}")

    # ---------- Operaciones ----------
    def register_book(self, item_id: int, title: str, author: str, publication_year: Optional[int], genre: str, quantity: int) -> Book:
        if item_id in self._items:
            raise ValueError("ID de item ya existe")
        book = Book(item_id, title, author, publication_year, genre, quantity)
        self._items[item_id] = book
        return book

    def register_magazine(self, item_id: int, title: str, issue: str, publication_year: Optional[int], quantity: int) -> Magazine:
        if item_id in self._items:
            raise ValueError("ID de item ya existe")
        mag = Magazine(item_id, title, issue, publication_year, quantity)
        self._items[item_id] = mag
        return mag

    def register_user(self, user_id: int, name: str) -> User:
        if user_id in self._users:
            raise ValueError("ID de usuario ya existe")
        u = User(user_id, name)
        self._users[user_id] = u
        return u

    def find_item(self, item_id: int) -> Optional[Item]:
        return self._items.get(item_id)

    def search_items(self, query: str) -> List[Item]:
        q = query.lower()
        results: List[Item] = []
        for it in self._items.values():
            if q in it.title.lower():
                results.append(it)
                continue
            # Book specific fields
            if isinstance(it, Book) and (q in it.author.lower() or q in it.genre.lower()):
                results.append(it)
            # Magazine specific fields
            if isinstance(it, Magazine) and q in it.issue.lower():
                results.append(it)
        return results

    def list_items(self) -> List[Item]:
        return list(self._items.values())

    def list_users(self) -> List[User]:
        return list(self._users.values())

    def issue_item(self, user_id: int, item_id: int) -> None:
        user = self._users.get(user_id)
        if not user:
            raise ValueError("Usuario no encontrado")
        item = self._items.get(item_id)
        if not item:
            raise ValueError("Item no encontrado")
        if item.quantity <= 0:
            raise ValueError("No hay unidades disponibles")
        # realizar préstamo
        success = item.decrement()
        if not success:
            raise ValueError("No se pudo decrementar la cantidad")
        user.issue(item_id)

    def return_item(self, user_id: int, item_id: int) -> None:
        user = self._users.get(user_id)
        if not user:
            raise ValueError("Usuario no encontrado")
        if not user.return_item(item_id):
            raise ValueError("El usuario no tiene prestado ese item")
        item = self._items.get(item_id)
        if not item:
            # Si el item ya no existe en el catálogo, creamos un placeholder con cantidad 1
            placeholder = Book(item_id, "Desconocido", "Desconocido", None, "Desconocido", 0)
            self._items[item_id] = placeholder
            item = placeholder
        item.increment()

    # ---------- Utilidades para la consola ----------
    def display_item(self, item: Item) -> None:
        print(item.display())

    def display_user(self, user: User) -> None:
        print(f"Usuario ID:{user.id} | {user.name} | Prestados: {len(user.issued_books)}")
        if user.issued_books:
            print("  Lista de prestados:")
            for bid in user.issued_books:
                it = self._items.get(bid)
                if it:
                    print("   -", it.display())
                else:
                    print(f"   - Item ID:{bid} (no existe en catálogo)")


# -----------------------------
# Interfaz de consola (menú)
# -----------------------------

def menu():
    lib = LibrarySystem()

    def safe_int(prompt: str) -> Optional[int]:
        v = input(prompt).strip()
        if v == "":
            return None
        try:
            return int(v)
        except ValueError:
            return None

    while True:
        print("\n=== Sistema de Biblioteca (POO) ===")
        print("1) Agregar libro")
        print("2) Agregar revista")
        print("3) Registrar usuario")
        print("4) Mostrar todos los items")
        print("5) Mostrar todos los usuarios")
        print("6) Buscar items (por texto)")
        print("7) Prestar item")
        print("8) Devolver item")
        print("9) Guardar datos")
        print("0) Salir")
        choice = input("Elige una opcion: ").strip()

        try:
            if choice == "1":
                iid = safe_int("ID del libro: ")
                if iid is None:
                    print("ID invalido")
                    continue
                title = input("Titulo: ").strip()
                author = input("Autor: ").strip()
                year = safe_int("Ano publicacion (opcional): ")
                genre = input("Genero: ").strip()
                qty = safe_int("Cantidad: ") or 1
                lib.register_book(iid, title, author, year, genre, qty)
                print("Libro registrado.")

            elif choice == "2":
                iid = safe_int("ID de la revista: ")
                if iid is None:
                    print("ID invalido")
                    continue
                title = input("Titulo: ").strip()
                issue = input("Edicion/Numero: ").strip()
                year = safe_int("Ano publicacion (opcional): ")
                qty = safe_int("Cantidad: ") or 1
                lib.register_magazine(iid, title, issue, year, qty)
                print("Revista registrada.")

            elif choice == "3":
                uid = safe_int("ID del usuario: ")
                if uid is None:
                    print("ID invalido")
                    continue
                name = input("Nombre: ").strip()
                lib.register_user(uid, name)
                print("Usuario registrado.")

            elif choice == "4":
                items = lib.list_items()
                if not items:
                    print("No hay items registrados.")
                for it in items:
                    lib.display_item(it)

            elif choice == "5":
                users = lib.list_users()
                if not users:
                    print("No hay usuarios registrados.")
                for u in users:
                    lib.display_user(u)

            elif choice == "6":
                q = input("Texto de busqueda: ").strip()
                if not q:
                    print("Consulta vacia")
                    continue
                res = lib.search_items(q)
                if not res:
                    print("No se encontraron items.")
                for it in res:
                    lib.display_item(it)

            elif choice == "7":
                uid = safe_int("ID usuario: ")
                iid = safe_int("ID item a prestar: ")
                if uid is None or iid is None:
                    print("ID invalido")
                    continue
                lib.issue_item(uid, iid)
                print("Prestamo realizado.")

            elif choice == "8":
                uid = safe_int("ID usuario: ")
                iid = safe_int("ID item a devolver: ")
                if uid is None or iid is None:
                    print("ID invalido")
                    continue
                lib.return_item(uid, iid)
                print("Devolucion realizada.")

            elif choice == "9":
                lib.save()
                print("Datos guardados.")

            elif choice == "0":
                print("Guardando antes de salir...")
                lib.save()
                print("Adios!")
                break

            else:
                print("Opcion no valida.")

        except Exception as e:
            print("Error:", e)


if __name__ == '__main__':
    menu()
