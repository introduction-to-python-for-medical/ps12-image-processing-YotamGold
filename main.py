clean_image = median(image, ball(3))
edge = edge_detection(clean_image)
binary_image = edge > 90
edge_image = Image.fromarray(binary_image)
edge_image.save('my_edges.png')

plt.imshow(binary_image, cmap='gray')
plt.show()
