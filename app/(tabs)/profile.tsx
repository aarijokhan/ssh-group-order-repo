import React from 'react';
import { View, Text, StyleSheet, SafeAreaView, ScrollView } from 'react-native';

export default function ProfileScreen() {
    return (
        <SafeAreaView style={styles.safeArea}> 
            <ScrollView contentContainerStyle={styles.container}>
                <View style={styles.header} >
                    <Text style={styles.headerText}>Your Profile</Text>
                    <Text style={styles.descriptionText}>Manage your profile, settings, and devices here.</Text>
                </View>
                <View style={styles.content}>
                    <Text style={styles.sectionTitle}>Profile Information</Text>
                    <Text style={styles.infoLabel}>Name: John Doe</Text>
                    <Text style={styles.infoLabel}>Email: john.doe@example.com</Text>
                    <Text style={styles.infoLabel}>Room Number: 12B</Text>
                </View>
             </ScrollView>
        </SafeAreaView>
    )
}
const styles = StyleSheet.create({
    safeArea: {
      flex: 1,
      backgroundColor: '#ffffff',
    },
    container: {
      alignItems: 'center',
      padding: 16,
    },
    header: {
      marginBottom: 24,
      alignItems: 'center'
    },
    headerText: {
      fontSize: 20, 
      fontWeight: 'bold',
      color: '#1d3d47',
      flex: 1,
      textAlign: 'center',
    },
    descriptionText: {
      fontSize: 16,
      color: '#666666',
      textAlign: 'center',
    },
    content: {
        backgroundColor: '#ffffff',
        borderRadius: 12,
        padding: 16,
        marginBottom: 16,
        shadowColor: '#000',
        shadowOpacity: 0.1,
        shadowOffset: { width: 0, height: 2 },
        shadowRadius: 8,
    },
    sectionTitle: {
        fontSize: 18,
        fontWeight: 'bold',
        marginBottom: 8,
        color: '#333333',
    },
    infoLabel: {
        fontSize: 16,
        color: '#333333',
        marginBottom: 4,
    }

}
);