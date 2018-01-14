import numpy as np
import h5py as h5py
import matplotlib.pyplot as plt

from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential, Model
from keras.layers import Dropout, Flatten, Dense
from keras import applications, optimizers


# dimensions of our images.
img_width, img_height = 150, 150

top_model_weights_path = 'bottleneck_VGG16_00.h5'
train_data_dir = 'data_00/train'
validation_data_dir = 'data_00/validation'
nb_train_samples = 5120
nb_validation_samples = 1280
epochs = 250
batch_size = 40


def save_bottlebeck_features():
	np.random.seed(2929)
	
	vgg_model = applications.VGG16(weights='imagenet', include_top=False, input_shape=(150, 150, 3))
	print('Model loaded.')

	#initialise top model
	top_model = Sequential()
	top_model.add(Flatten(input_shape=vgg_model.output_shape[1:]))
	top_model.add(Dense(256, activation='relu'))
	top_model.add(Dropout(0.5))
	top_model.add(Dense(1, activation='sigmoid'))

        model = Model(inputs=vgg_model.input, outputs=top_model(vgg_model.output))

        model.trainable = True

        model.summary()

	#Total of 20 layers. The classification is considered as one layer
        #Therefore, intermediate is 19 layers
        #0, 4[:4], 3[:7], 4[:11], 4[:15], 4[:19] (Group 0, 1, 2, 3, 4, 5)
        #0 -> All trainable
        #5 -> All non-trainable except classification layer
        #Always keep layer 20 trainable because it is classification layer
        #layer_count = 1
        for layer in model.layers[:11]:
            layer.trainable = False
	    #print("NO-Top: Layer is %d trainable" %layer_count)  
	    #layer_count = layer_count + 1

        model.summary()


        train_datagen = ImageDataGenerator(rescale=1. / 255)
        test_datagen = ImageDataGenerator(rescale=1. / 255)

        train_generator = train_datagen.flow_from_directory(
            train_data_dir,
            target_size=(img_height, img_width),
            batch_size=batch_size,
            class_mode='binary')

        validation_generator = test_datagen.flow_from_directory(
            validation_data_dir,
            target_size=(img_height, img_width),
            batch_size=batch_size,
            class_mode='binary')

	sgd = optimizers.Adam(lr=1e-6) #optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)

	model.compile( loss = "binary_crossentropy", 
            optimizer = sgd, 
            metrics=['accuracy']
            )

#        model.compile(optimizer='rmsprop',
#            loss='binary_crossentropy', metrics=['accuracy'])

        history = model.fit_generator(
	    train_generator,
            steps_per_epoch=nb_train_samples // batch_size,
            epochs=epochs,
            validation_data=validation_generator,
            validation_steps=nb_validation_samples // batch_size,
            verbose=1)

        history_dict =  history.history

        #Plotting the training and validation loss
        history_dict = history.history
        loss_values = history_dict['loss']
        val_loss_values = history_dict['val_loss']
        epochs_0 = range(1, len(history_dict['acc']) + 1)
        plt.plot(epochs_0, loss_values, 'bo', label='Training loss')
        plt.plot(epochs_0, val_loss_values, 'b', label='Validation loss')
        plt.title('Freeze Group 3 - Training and validation loss')
        plt.xlabel('Epochs')
        plt.ylabel('Loss')
        plt.legend()
        plt.show()

        #Plotting the training and validation accuracy
        acc_values = history_dict['acc']
        val_acc_values = history_dict['val_acc']
        plt.plot(epochs_0, acc_values, 'bo', label='Training acc')
        plt.plot(epochs_0, val_acc_values, 'b', label='Validation acc')
        plt.title('Freeze Group 3 - Training and validation accuracy')
        plt.xlabel('Epochs')
        plt.ylabel('Loss')
        plt.legend()
        plt.show()


save_bottlebeck_features()















############################
############################
# OLD CODE, MAY BE USEFUL LATER
############################
############################
#        datagen = ImageDataGenerator(rescale=1. / 255)

#        generator = datagen.flow_from_directory(
#            train_data_dir,
#            target_size=(img_width, img_height),
#            batch_size=batch_size,
#            class_mode=None,
#            shuffle=False)
#        bottleneck_features_train = model.predict_generator(
#            generator, nb_train_samples // batch_size)
#        np.save(open('bottleneck_features_train.npy', 'w'),
#            bottleneck_features_train)

#        generator = datagen.flow_from_directory(
#            validation_data_dir,
#            target_size=(img_width, img_height),
#            batch_size=batch_size,
#            class_mode=None,
#            shuffle=False)
#        bottleneck_features_validation = model.predict_generator(
#            generator, nb_validation_samples // batch_size)
#        np.save(open('bottleneck_features_validation.npy', 'w'),
#            bottleneck_features_validation)

#        train_data = np.load(open('bottleneck_features_train.npy'))
#        train_labels = np.array(
#            [0] * (nb_train_samples / 2) + [1] * (nb_train_samples / 2))

#        validation_data = np.load(open('bottleneck_features_validation.npy'))
#        validation_labels = np.array(
#            [0] * (nb_validation_samples / 2) + [1] * (nb_validation_samples / 2))


#        model.compile(optimizer='rmsprop',
#            loss='binary_crossentropy', metrics=['accuracy'])

#        model.fit(train_data, train_labels,
#            epochs=epochs,
#            batch_size=batch_size,
#            validation_data=(validation_data, validation_labels))


#####

#history = model.fit(train_data, train_labels,
    #          epochs=epochs,
    #          batch_size=batch_size,
    #          validation_data=(validation_data, validation_labels))
    #


    #history_dict =  history.history

    #Plotting the training and validation loss
    #history_dict = history.history
    #loss_values = history_dict['loss']
    #val_loss_values = history_dict['val_loss']
    #epochs_0 = range(1, len(history_dict['acc']) + 1)
    #plt.plot(epochs_0, loss_values, 'bo', label='Training loss')
    #plt.plot(epochs_0, val_loss_values, 'b', label='Validation loss')
    #plt.title('Freeze Group 5 - Training and validation loss')
    #plt.xlabel('Epochs')
    #plt.ylabel('Loss')
    #plt.legend()
    #plt.show()

    #Plotting the training and validation accuracy
    #acc_values = history_dict['acc']
    #val_acc_values = history_dict['val_acc']
    #plt.plot(epochs_0, acc_values, 'bo', label='Training acc')
    #plt.plot(epochs_0, val_acc_values, 'b', label='Validation acc')
    #plt.title('Freeze Group 5 - Training and validation accuracy')
    #plt.xlabel('Epochs')
    #plt.ylabel('Loss')
    #plt.legend()
    #plt.show()

