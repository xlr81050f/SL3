import os
import django
from datetime import date

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')
django.setup()

# Import the Book model after Django setup
from books.models import Book

# Sample books data
sample_books = [
    {
        'title': 'Artificial Intelligence: A Modern Approach',
        'author': 'Stuart Russell & Peter Norvig',
        'description': 'Comprehensive introduction to the theory and practice of artificial intelligence.',
        'price': 720,
        'inventory': 15,
        'cover_image': 'https://m.media-amazon.com/images/I/51xYYKI1WRL._SX440_BO1,204,203,200_.jpg',
    },
    {
        'title': 'Machine Learning: The New AI',
        'author': 'Ethem Alpaydin',
        'description': 'Overview of machine learning, its evolution, and applications.',
        'price': 1500,
        'inventory': 10,
        'cover_image': 'https://m.media-amazon.com/images/I/41KCMUX7WyL._SX331_BO1,204,203,200_.jpg',
    },
    {
        'title': 'Python Crash Course',
        'author': 'Eric Matthes',
        'description': 'A fast-paced, thorough introduction to Python programming.',
        'price': 800,
        'inventory': 20,
        'cover_image': 'https://m.media-amazon.com/images/I/51j89lmxALL._SX377_BO1,204,203,200_.jpg',
    },
    {
        'title': 'Learning Python',
        'author': 'Mark Lutz',
        'description': 'In-depth introduction to the core Python language.',
        'price': 950,
        'inventory': 12,
        'cover_image': 'https://m.media-amazon.com/images/I/51RI7tLJmFL._SX379_BO1,204,203,200_.jpg',
    },
    {
        'title': 'Effective Java',
        'author': 'Joshua Bloch',
        'description': 'Best practices for writing robust and maintainable Java code.',
        'price': 1100,
        'inventory': 8,
        'cover_image': 'https://m.media-amazon.com/images/I/41zLisPNN2L._SX376_BO1,204,203,200_.jpg',
    },
    {
        'title': 'Java: The Complete Reference',
        'author': 'Herbert Schildt',
        'description': 'Comprehensive guide to the Java programming language.',
        'price': 1200,
        'inventory': 15,
        'cover_image': 'https://m.media-amazon.com/images/I/51U-Fm7qQQL._SX218_BO1,204,203,200_QL40_FMwebp_.jpg',
    },
    {
        'title': 'The C Programming Language',
        'author': 'Brian W. Kernighan & Dennis M. Ritchie',
        'description': 'Classic introduction to the C programming language.',
        'price': 600,
        'inventory': 7,
        'cover_image': 'https://m.media-amazon.com/images/I/411ejyE8obL._SX377_BO1,204,203,200_.jpg',
    },
    {
        'title': 'C++ Primer',
        'author': 'Stanley B. Lippman, Josée Lajoie, & Barbara E. Moo',
        'description': 'Comprehensive introduction to C++ programming.',
        'price': 1300,
        'inventory': 10,
        'cover_image': 'https://m.media-amazon.com/images/I/51YdKzrOQFL._SX380_BO1,204,203,200_.jpg',
    },
    {
        'title': 'Discrete Mathematics and Its Applications',
        'author': 'Kenneth H. Rosen',
        'description': 'Comprehensive guide to discrete mathematics.',
        'price': 1400,
        'inventory': 5,
        'cover_image': 'https://m.media-amazon.com/images/I/51OZJvgDGLL._SX409_BO1,204,203,200_.jpg',
    },
    {
        'title': 'Introduction to the Theory of Computation',
        'author': 'Michael Sipser',
        'description': 'Introduction to the fundamental concepts of computational theory.',
        'price': 1250,
        'inventory': 6,
        'cover_image': 'https://m.media-amazon.com/images/I/51rlJpxQIAL._SX258_BO1,204,203,200_.jpg',
    },
    {
        'title': 'Django for Beginners',
        'author': 'William S. Vincent',
        'description': 'Learn to build web applications with Django.',
        'price': 700,
        'inventory': 18,
        'cover_image': 'https://m.media-amazon.com/images/I/41oN+0bIJ7L._SX331_BO1,204,203,200_.jpg',
    },
    {
        'title': 'Two Scoops of Django',
        'author': 'Daniel Roy Greenfeld & Audrey Roy Greenfeld',
        'description': 'Best practices for the Django web framework.',
        'price': 1600,
        'inventory': 9,
        'cover_image': 'https://m.media-amazon.com/images/I/51GXJ-HaHRL._SX260_BO1,204,203,200_.jpg',
    },
    {
        'title': 'Web Development with Django',
        'author': 'Ben Shaw, Saurabh Badhwar, Andrew Bird, & Aidas Bendoraitis',
        'description': 'Comprehensive guide to web development using Django.',
        'price': 1800,
        'inventory': 7,
        'cover_image': 'https://m.media-amazon.com/images/I/41Ygz3JxgeL._SX404_BO1,204,203,200_.jpg',
    },
    {
        'title': 'Deep Learning',
        'author': 'Ian Goodfellow, Yoshua Bengio, & Aaron Courville',
        'description': 'Comprehensive introduction to deep learning.',
        'price': 1900,
        'inventory': 12,
        'cover_image': 'https://m.media-amazon.com/images/I/61qbj4KwauL._SX387_BO1,204,203,200_.jpg',
    },
    {
        'title': 'Pattern Recognition and Machine Learning',
        'author': 'Christopher M. Bishop',
        'description': 'Introduction to pattern recognition and machine learning.',
        'price': 1700,
        'inventory': 8,
        'cover_image': 'https://m.media-amazon.com/images/I/61BmZ0LrQvL._SX429_BO1,204,203,200_.jpg',
    },
    {
        'title': 'Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow',
        'author': 'Aurélien Géron',
        'description': 'Practical guide to machine learning with Python.',
        'price': 1500,
        'inventory': 15,
        'cover_image': 'https://m.media-amazon.com/images/I/51aqYc1QyrL._SX379_BO1,204,203,200_.jpg',
    },
    {
        'title': 'Introduction to Algorithms',
        'author': 'Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, & Clifford Stein',
        'description': 'Comprehensive introduction to algorithms.',
        'price': 2000,
        'inventory': 10,
        'cover_image': 'https://m.media-amazon.com/images/I/41T0iBxY8FL._SX258_BO1,204,203,200_.jpg',
    },
    {
        'title': 'Computer Networking: A Top-Down Approach',
        'author': 'James F. Kurose & Keith W. Ross',
        'description': 'Introduction to computer networking principles.',
        'price': 1350,
        'inventory': 12,
        'cover_image': 'https://m.media-amazon.com/images/I/51xp1+zTG8L._SX258_BO1,204,203,200_.jpg',
    },
    {
        'title': 'Operating System Concepts',
        'author': 'Abraham Silberschatz, Peter B. Galvin, & Greg Gagne',
        'description': 'Comprehensive guide to operating system principles.',
        'price': 1450,
        'inventory': 9,
        'cover_image': 'https://m.media-amazon.com/images/I/51Qy2upM+aL._SX258_BO1,204,203,200_.jpg',
    },
    {
        'title': 'Docker Deep Dive',
        'author': 'Nigel Poulton',
        'description': 'Comprehensive guide to Docker containers and containerization.',
        'price': 1299,
        'inventory': 14,
        'cover_image': 'https://m.media-amazon.com/images/I/41QgNUUtJ9L._SX331_BO1,204,203,200_.jpg',
    },
    {
        'title': 'Kubernetes: Up and Running',
        'author': 'Brendan Burns, Joe Beda & Kelsey Hightower',
        'description': 'Dive into the world of container orchestration with Kubernetes.',
        'price': 1599,
        'inventory': 11,
        'cover_image': 'https://m.media-amazon.com/images/I/51Vpt6bhKOL._SX379_BO1,204,203,200_.jpg',
    },
    {
        'title': 'Blockchain Basics: A Non-Technical Introduction',
        'author': 'Daniel Drescher',
        'description': 'A non-technical introduction to the fundamentals of blockchain technology.',
        'price': 1199,
        'inventory': 16,
        'cover_image': 'https://m.media-amazon.com/images/I/41oQkVLDiLL._SX313_BO1,204,203,200_.jpg',
    },
    {
        'title': 'Python for Data Analysis',
        'author': 'Wes McKinney',
        'description': 'Data analysis and manipulation with pandas, NumPy, and IPython.',
        'price': 1399,
        'inventory': 13,
        'cover_image': 'https://m.media-amazon.com/images/I/51Oa3JZQzrL._SX389_BO1,204,203,200_.jpg',
    },
    {
        'title': 'NumPy Cookbook',
        'author': 'Ivan Idris',
        'description': 'Recipes for scientific computing with Python and NumPy.',
        'price': 1099,
        'inventory': 8,
        'cover_image': 'https://m.media-amazon.com/images/I/51GxW8imsoL._SX404_BO1,204,203,200_.jpg',
    },
]

def populate_books():
    # Clear existing books
    Book.objects.all().delete()
    
    # Add new books
    for book_data in sample_books:
        Book.objects.create(**book_data)
    
    # Print summary
    print(f"Added {len(sample_books)} books to the database.")
    print("Sample of books added:")
    for book in Book.objects.all()[:5]:
        print(f" - {book.title} by {book.author} (₹{book.price})")

if __name__ == '__main__':
    print("Starting book population script...")
    populate_books()
    print("Book population completed!")