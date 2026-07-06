# CrudMVC

A simple desktop CRUD application built with **Tkinter** (View), **MongoDB** (Model), following the **MVC** (Model-View-Controller) pattern. It lets you register products with a name, stock quantity, and picture, then search for them.

## Structure

| File   | Role       | Description                                                      |
|--------|------------|-------------------------------------------------------------------|
| `M.py` | Model      | Handles MongoDB connection and CRUD operations on the `products` collection, including storing product images as binary data. |
| `V.py` | View       | Tkinter GUI: main screen (register product), search screen, and edit screen. |
| `C.py` | Controller | Mediates between the View and the Model, handles file selection and validation. |

## Requirements

- Python 3
- [pymongo](https://pypi.org/project/pymongo/)
- [Pillow](https://pypi.org/project/Pillow/)

Install dependencies:

```bash
pip install pymongo pillow
```

## Configuration

The Model connects to a MongoDB Atlas cluster using credentials from environment variables:

- `root` — MongoDB username
- `password` — MongoDB password
- `cluster` — MongoDB cluster connection suffix (e.g. `@cluster0.mongodb.net/?retryWrites=true&w=majority`)

Set these before running the app, for example:

```bash
export root=your_username
export password=your_password
export cluster=@your-cluster-url
```

## Running

```bash
python V.py
```

This opens the main window where you can:

- Register a new product (name, stock, and a picture from disk)
- Search for existing products
- Edit or delete a product

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.
