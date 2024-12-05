import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, SafeAreaView, ScrollView, TouchableOpacity, Alert } from 'react-native';
import axios from 'axios';

type Product = {
  id: string;
  name: string;
  price: number;
  category: string;
};

export default function MarketplaceScreen() {
  const [products, setProducts] = useState<Product[]>([]);  // Define the type explicitly
  const [cart, setCart] = useState<Product[]>([]);  // Define the type explicitly
  const [selectedCategory, setSelectedCategory] = useState<string | null>(null);  // Type for selected category

  // Function to fetch products from the backend
  const fetchProducts = async () => {
    try {
      const response = await axios.get('http://10.115.206.210:8000/products');
      setProducts(response.data); 
    } catch (error) {
      console.error('Error fetching products:', error);
    }
  };

  // Fetch the products when the component mounts
  useEffect(() => {
    fetchProducts();
  }, []);

  // Get unique categories from the products
  const getCategories = () => {
    const categories = products.map((product) => product.category);
    return [...new Set(categories)];
  };

  // Function to add product to cart
  const addToCart = (product: Product) => {
    setCart((prevCart) => [...prevCart, product]);
    Alert.alert('Product Added', `${product.name} has been added to your cart.`);
  };

  // Function to view cart total
  const getCartTotal = () => {
    return cart.reduce((total, product) => total + product.price, 0).toFixed(2);
  };

  return (
    <SafeAreaView style={styles.safeArea}>
      <ScrollView contentContainerStyle={styles.container}>
        <Text style={styles.headerText}>Marketplace</Text>

        {/* Display categories */}
        <Text style={styles.subHeaderText}>Categories:</Text>
        <ScrollView horizontal showsHorizontalScrollIndicator={false} style={styles.categoriesContainer}>
          {getCategories().map((category) => (
            <TouchableOpacity
              key={category}
              style={styles.categoryButton}
              onPress={() => setSelectedCategory(category)}
            >
              <Text style={styles.categoryText}>{category}</Text>
            </TouchableOpacity>
          ))}
        </ScrollView>

        {/* Display products */}
        <Text style={styles.subHeaderText}>Products:</Text>
        {products.length > 0 ? (
          products
            .filter((product) => !selectedCategory || product.category === selectedCategory)
            .map((product) => (
              <View key={product.id} style={styles.productCard}>
                <Text style={styles.productName}>{product.name}</Text>
                <Text style={styles.productPrice}>£{product.price.toFixed(2)}</Text>
                <Text style={styles.productCategory}>{product.category}</Text>
                <TouchableOpacity style={styles.addButton} onPress={() => addToCart(product)}>
                  <Text style={styles.addButtonText}>Add to Cart</Text>
                </TouchableOpacity>
              </View>
            ))
        ) : (
          <Text style={styles.noProductsText}>No products available.</Text>
        )}

        {/* Cart Summary */}
        <View style={styles.cartContainer}>
          <Text style={styles.cartHeaderText}>Your Cart</Text>
          {cart.length > 0 ? (
            <>
              {cart.map((product, index) => (
                <View key={index} style={styles.cartItem}>
                  <Text style={styles.cartItemText}>{product.name} - £{product.price.toFixed(2)}</Text>
                </View>
              ))}
              <Text style={styles.cartTotalText}>Total: £{getCartTotal()}</Text>
              <TouchableOpacity
                style={styles.checkoutButton}
                onPress={() => Alert.alert('Checkout', `Total: £${getCartTotal()}\nCheckout Successful!`)}
              >
                <Text style={styles.checkoutButtonText}>Checkout</Text>
              </TouchableOpacity>
            </>
          ) : (
            <Text style={styles.noProductsText}>Your cart is empty.</Text>
          )}
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: '#f9f9f9',
  },
  container: {
    padding: 16,
  },
  headerText: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#1d3d47',
    textAlign: 'center',
    marginBottom: 16,
  },
  subHeaderText: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#1d3d47',
    marginBottom: 8,
  },
  categoriesContainer: {
    marginBottom: 16,
  },
  categoryButton: {
    backgroundColor: '#1d3d47',
    borderRadius: 8,
    paddingVertical: 8,
    paddingHorizontal: 16,
    marginRight: 8,
  },
  categoryText: {
    color: '#ffffff',
    fontSize: 14,
    fontWeight: 'bold',
  },
  productCard: {
    backgroundColor: '#ffffff',
    borderRadius: 8,
    padding: 16,
    marginBottom: 16,
    shadowColor: '#000',
    shadowOpacity: 0.1,
    shadowOffset: { width: 0, height: 2 },
    shadowRadius: 8,
  },
  productName: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#333333',
    marginBottom: 4,
  },
  productPrice: {
    fontSize: 16,
    color: '#1d3d47',
    marginBottom: 4,
  },
  productCategory: {
    fontSize: 14,
    color: '#666666',
    marginBottom: 8,
  },
  addButton: {
    backgroundColor: '#ffa500',
    borderRadius: 8,
    paddingVertical: 8,
    paddingHorizontal: 16,
    alignItems: 'center',
  },
  addButtonText: {
    color: '#ffffff',
    fontSize: 16,
    fontWeight: 'bold',
  },
  cartContainer: {
    marginTop: 24,
    padding: 16,
    borderRadius: 8,
    backgroundColor: '#ffffff',
    shadowColor: '#000',
    shadowOpacity: 0.1,
    shadowOffset: { width: 0, height: 2 },
    shadowRadius: 8,
  },
  cartHeaderText: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#1d3d47',
    marginBottom: 16,
  },
  cartItem: {
    marginBottom: 8,
  },
  cartItemText: {
    fontSize: 16,
    color: '#333333',
  },
  cartTotalText: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#1d3d47',
    marginTop: 16,
  },
  checkoutButton: {
    backgroundColor: '#1d3d47',
    borderRadius: 8,
    paddingVertical: 12,
    paddingHorizontal: 24,
    marginTop: 16,
    alignItems: 'center',
  },
  checkoutButtonText: {
    color: '#ffffff',
    fontSize: 16,
    fontWeight: 'bold',
  },
  noProductsText: {
    fontSize: 16,
    textAlign: 'center',
    color: '#666666',
    marginBottom: 16,
  },
});
