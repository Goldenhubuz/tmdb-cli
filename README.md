# Tmdb-App forked for testing

**Tmdb-App** is a command-line application to explore information about movies using the TMDB API. You can search for popular, currently playing, top-rated, and upcoming movies.

### **Requirements**

To run the application, make sure you have the following dependencies installed:

```bash
pip install -r requirements.txt
```

### **How to Run the Application**

To run the application, use the following command:

```bash
# Windows OS
python3 main.py movies --type <type>

# Linux
alias tmdb-app="python3 main.py movies"
tmdb-app --type <type>
```

The types of movies you can search for are:

- `popular`: Popular movies.
- `playing`: Currently playing movies.
- `top`: Top-rated movies.
- `upcoming`: Upcoming releases.

### **Usage Examples**

1. **Search for popular movies:**

   ```bash
   python3 main.py movies --type popular
   ```

   This command displays a list of the most popular movies currently.

2. **Search for currently playing movies:**

   ```bash
   python3 main.py movies --type playing
   ```

   This command displays a list of movies currently in theaters.

3. **Search for top-rated movies:**

   ```bash
   python3 main.py movies --type top
   ```

   This command displays a list of the top-rated movies.

4. **Search for upcoming releases:**

   ```bash
   python3 main.py movies --type upcoming
   ```

   This command displays a list of upcoming movie releases.

### **Dependencies**

- **Typer**: For creating the command-line interface.
- **Requests**: For making HTTP requests to the TMDB API.
- **Others**: Be sure to check `requirements.txt` for other necessary dependencies.

### **Contact**

If you have any questions or suggestions, feel free to contact the development team at [jaracalle2041@gmail.com](jaracalle2041@gmail.com), project developed for [Roadmap.sh](https://roadmap.sh/projects/tmdb-cli).

